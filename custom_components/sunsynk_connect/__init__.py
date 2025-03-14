from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from .const import DOMAIN, SCAN_INTERVAL
from datetime import timedelta
import requests
import logging

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up SunSynkConnect component (YAML not supported)."""
    return True  # Don't use YAML, we handle config in config flow

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up SunSynkConnect from a config entry."""
    username = entry.data["username"]
    password = entry.data["password"]
    serial = entry.data["serial"]

    coordinator = SunSynkCoordinator(hass, username, password, serial)

    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator

    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    await hass.config_entries.async_forward_entry_unload(entry, "sensor")

    hass.data[DOMAIN].pop(entry.entry_id)

    return True

class SunSynkCoordinator(DataUpdateCoordinator):
    """Class to manage fetching SunSynk data."""

    def __init__(self, hass, username, password, serial):
        self.username = username
        self.password = password
        self.serial = serial
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=SCAN_INTERVAL),
        )

    async def _async_update_data(self):
        """Fetch data from SunSynk API."""
        try:
            # Example login flow
            login_response = requests.post(
                "https://api.sunsynk.io/v1/login",
                json={"username": self.username, "password": self.password},
                timeout=10
            )
            login_response.raise_for_status()

            token = login_response.json().get("token")

            # Use the token to fetch the data
            data_response = requests.get(
                "https://api.sunsynk.io/v1/data",
                headers={"Authorization": f"Bearer {token}"},
                timeout=10
            )
            data_response.raise_for_status()

            return data_response.json()
        except requests.RequestException as err:
            raise UpdateFailed(f"API request failed: {err}") from err


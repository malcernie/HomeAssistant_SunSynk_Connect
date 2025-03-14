from homeassistant.helpers.entity import Entity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up SunSynk sensors from config entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities([SunSynkSensor(coordinator)], True)

class SunSynkSensor(Entity):
    """Sensor for SunSynk data."""

    def __init__(self, coordinator):
        """Initialize the sensor."""
        self.coordinator = coordinator
        self._name = "SunSynk Power Sensor"

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        """Return sensor state."""
        return self.coordinator.data.get("power")

    @property
    def extra_state_attributes(self):
        """Return additional sensor attributes."""
        return self.coordinator.data

    async def async_update(self):
        """Update sensor manually."""
        await self.coordinator.async_request_refresh()


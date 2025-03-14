import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback

from .const import DOMAIN

DATA_SCHEMA = vol.Schema({
    vol.Required("username"): str,
    vol.Required("password"): str,
    vol.Required("serial"): str
})

class SunSynkConnectConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for SunSynkConnect."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            # Here you would validate credentials against the API.
            username = user_input["username"]
            password = user_input["password"]
            serial = user_input["serial"]

            # You can optionally validate the credentials here by testing the API.
            valid = await self._async_validate_credentials(username, password)

            if valid:
                return self.async_create_entry(
                    title=f"SunSynk: {username}",
                    data=user_input,
                )
            else:
                errors["base"] = "auth_failed"

        return self.async_show_form(
            step_id="user",
            data_schema=DATA_SCHEMA,
            errors=errors
        )

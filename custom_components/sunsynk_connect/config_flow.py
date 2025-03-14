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
    MINOR_VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            # Here you would validate credentials against the API.
            username = user_input["username"]
            password = user_input["password"]
            serial = user_input["serial"]

            if (len(username) > 0 AND
                len(password) > 0 AND
                len (serial) > 0):
                return self.async_create_entry(
                    title=f"SunSynk_Connect: {username}",
                    data=user_input,
                )
            else:
                errors["base"] = "requires all fields"

        return self.async_show_form(
            step_id="user",
            data_schema=DATA_SCHEMA,
            errors=errors
        )


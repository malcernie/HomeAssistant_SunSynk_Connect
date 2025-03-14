# Base component constants
NAME = "Sunsynk Connect"
DOMAIN = "sunsynk_connect"
VERSION = "0.0.1"

ATTRIBUTION = "Data provided by Sunsynk Connect"
ISSUE_URL = "https://github.com/malcernie/HomeAssistant_SunSynk_Connect/issues"

# Icons
ICON = "mdi:format-quote-close"

# Platforms
SENSOR = "sensor"
BINARY_SENSOR = "binary_sensor"
SELECT = "select"
NUMBER = "number"
SWITCH = "switch"
PLATFORMS = [SENSOR, BINARY_SENSOR, SELECT, NUMBER, SWITCH]


# Configuration and options
CONF_SCAN_INTERVAL = 60
CONF_USERNAME = "username"
CONF_PASSWORD = "password"

# Defaults
DEFAULT_NAME = DOMAIN


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""

# HomeAssistant_SunSynk_Connect
Unofficial Home Assistant integration to the SunSynk Connect cloud platform.

# Sensors
table

# Actions
| Action | Parameters | Payload |
| - | - | - |
| Start Grid Charge | BatteryTarget {detault: 100) | Instructs inverter to charge from grid to the target battery percent by enabling user timer and setting grid charge variable.  Calls "Set User Timer".|
| Stop Grid Charge | (none) | Instructs inverter to stop charging from grid by disabling the user timer. Calls "Disable User Timer" |
| Set User Timer | Time1, Power1, Battery1, Grid1, Generator1, .... , Time6, Power6, Battery6, Grid6, Generator6 | Turns on the user timer and sets the schedule as per parameters |
| Disable User Timer | (none) | Turns off the user timer |

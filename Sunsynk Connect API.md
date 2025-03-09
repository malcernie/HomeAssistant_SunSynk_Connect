# Authentication

# Listing Inverters
Request URL: https://api.sunsynk.net/api/v1/inverters?page=1&limit=10&total=0&status=-1&sn=&plantId=&type=-2&softVer=&hmiVer=&agentCompanyId=-1&gsn=

Request Method: GET

Request Headers:
| Header | Value |
| -------- | ------- |
| Authorization | Bearer {TOKEN} |

Expected Response:
```
{
    "code": 0,
    "msg": "Success",
    "data": {
        "pageSize": 10,
        "pageNumber": 1,
        "total": 1,
        "infos": [
            {
                "id": [inverterId],
                "sn": "[inverterSerialNumber]",
                "alias": "[alias]",
                "gsn": "[gatewaySerialNumber]",
                "status": 1,
                "type": 2,
                "commTypeName": "RS485",
                "custCode": 29,
                "version": {
                    "masterVer": "2.3.8.2",
                    "softVer": "1.5.1.5",
                    "hardVer": "",
                    "hmiVer": "E.4.2.6",
                    "bmsVer": "",
                    "commVer": null
                },
                "model": "",
                "equipMode": null,
                "pac": 0,
                "etoday": 0.00,
                "etotal": 0.00,
                "updateAt": "2025-03-08T23:44:05Z",
                "opened": 1,
                "plant": {
                    "id": [plantId],
                    "name": "[plantName]",
                    "type": 2,
                    "master": null,
                    "installer": null,
                    "email": null,
                    "phone": null
                },
                "gatewayVO": {
                    "gsn": "[gatewaySerialNumber]",
                    "status": 2
                },
                "sunsynkEquip": true,
                "protocolIdentifier": "2",
                "equipType": 2
            }
        ]
    },
    "success": true
}
```

# Inverter Information
Request URL: https://api.sunsynk.net/api/v1/inverter/{inverterSerialNumber}

Request Method: GET

Request Headers:
| Header | Value |
| -------- | ------- |
| Authorization | Bearer {TOKEN} |

Expected Response:
```
```

# Inverter Settings
Request URL: https://api.sunsynk.net/api/v1/common/setting/{inverterSerialNumber}/read

Request Method: GET

Request Headers:
| Header | Value |
| -------- | ------- |
| Authorization | Bearer {TOKEN} |

Expected Response:
```
{
    "code": 0,
    "msg": "Success",
    "data": {
        ** Battery Settings **
        "battType": "0",
        "batteryCap": "315",
        "batteryMaxCurrentDischarge": "80",
        "batteryMaxCurrentCharge": "40",
        "batteryShutdownCap": "10",
        "batteryRestartCap": "50",
        "batteryLowCap": "12",

        "bmsErrStop": "0",
        "isletProtect": "0",

        "batteryEmptyV": "45",
        "batteryEmptyVolt": "45",


        ** System Mode **
        "sysWorkMode": "2",                           -> sunsynk_{inverterSerialNumber}_work_mode
        "solarSell": "0",                             -> sunsynk_{inverterSerialNumber}_solar_export
        "peakAndVallery": "1",                        -> sunsynk_{inverterSerialNumber}_user_timer
        "pvMaxLimit": "3000",
        "energyMode": "1",
        "zeroExportPower": "30",
        "time1on": "true",
        "time2on": "true",
        "time3on": "false",
        "time4on": "false",
        "time5on": "false",
        "time6on": "true",
        "time1On": "1",
        "time2On": "1",
        "time3On": "0",
        "time4On": "0",
        "time5On": "0",
        "time6On": "1",
        "genTime1on": "false",
        "genTime2on": "false",
        "genTime3on": "false",
        "genTime4on": "false",
        "genTime5on": "false",
        "genTime6on": "false",
        "sellTime1": "00:00",
        "sellTime1Pac": "3000",
        "cap1": "95",
        "sellTime2": "05:00",
        "sellTime2Pac": "3000",
        "cap2": "100",
        "sellTime3": "05:30",
        "sellTime3Pac": "3000",
        "cap3": "15",
        "sellTime4": "08:30",
        "sellTime4Pac": "3000",
        "cap4": "15",
        "sellTime5": "12:00",
        "sellTime5Pac": "3000",
        "cap5": "15",
        "sellTime6": "23:30",
        "sellTime6Pac": "3000",
        "cap6": "80",


        ** Grid Settings **
        "gridMode": "0",

        "importPower": "850",


        ** Auxiliary Load **

        ** Basic Settings **
        "timeSync": "1",
        "beep": "1",
        "lockOutChange": "0",
        "ampm": "0",
        "autoDim": "1",



        ** Advanced Settings **


        ** The Rest **
        "wattOverExitFreqStopDelay": "0",
        "exMeterCtSwitch": "0",
        "sdChargeOn": "1",
        "lockInVoltVar": "20.0",
        "batWarn": "0",
        "wattVarEnable": "13959",
        "reconnMinVolt": "187",
        "caFStart": "50.2",
        "sensorsCheck": "-1",
        "underFreq2Delay": "0.1",
        "varQac2": "0",
        "varQac3": "0",
        "varQac1": "44",
        "wattUnderExitFreq": "49.8",
        "overVolt1": "265",
        "overVolt2": "265",
        "varQac4": "-60",
        "genPeakPower": "8000",
        "meterB": "0",
        "eeprom": "0",
        "meterA": "0",
        "comSet": "3823",
        "caVoltPressureEnable": "0",
        "meterC": "0",
        "wattUnderFreq1": "49.8",
        "solarMaxSellPower": "3800",
        "acCoupleOnGridSideEnable": "0",
        "thursdayOn": "true",
        "overFreq1Delay": "0.1",
        "checkTime": "10",
        "atsSwitch": "0",
        "acCurrentUp": "0",
        "rsd": "1",
        "batteryOn": "0",
        "volt12": "490",
        "volt10": "300",
        "volt11": "490",
        "wattUnderFreq1StartDelay": "0",
        "rcd": "0",
        "chargeVolt": "57.6",
        "wednesdayOn": "true",
        "mpptMulti": "0",
        "floatVolt": "55.2",
        "workState": "0",
        "loadMode": "0",
        "sn": "{inverterSerialNumber}",
        "genCoolingTime": "0",
        "genPeakShaving": "0",
        "offGridImmediatelyOff": "0",
        "sellTime3Volt": "49",
        "current12": "0",
        "current10": "0",
        "current11": "0",
        "batteryEfficiency": "99",
        "genAndGridSignal": "3",
        "wattV4": "111.0",
        "acFreqLow": "0",
        "wattV2": "110.0",
        "wattV3": "111.0",
        "wattV1": "109.0",
        "open": "1",
        "reconnMaxFreq": "51.3",
        "standard": "0",
        "wattVarReactive2": "-327",
        "disableFloatCharge": "0",
        "inverterType": "0",
        "wattVarReactive3": "-125",
        "wattVarReactive4": "156",
        "solarPSU": "0",
        "fridayOn": "true",
        "wattVarReactive1": "182",
        "generatorForcedStart": "0",
        "overLongVolt": "260",
        "batteryChargeType": "1",
        "genOffVolt": "51",
        "absorptionVolt": "57.6",
        "genToLoad": "0",
        "mpptNum": "0",
        "underFreq2": "48",
        "underFreq1": "48",
        "wattPfEnable": "1457",
        "remoteLock": "0",
        "generatorStartCap": "30",
        "overFreq1": "51.5",
        "tuesdayOn": "true",
        "genOnVolt": "54",
        "overFreq2": "51.5",
        "solar2WindInputEnable": "60",
        "caVStop": "253",
        "battMode": "-1",
        "allowRemoteControl": "0",
        "genOnCap": "100",
        "gridAlwaysOn": "0",
        "batteryLowVolt": "47.5",
        "acFreqUp": "0",
        "chargeLimit": "0",
        "generatorStartVolt": "49",
        "overVolt1Delay": "0.1",
        "californiaFreqPressureEnable": "-1",
        "activePowerControl": "0",
        "batteryRestartVolt": "52",
        "overVolt2Delay": "0.1",
        "equChargeCycle": "90",
        "dischargeCurrent": "80",
        "mpptVoltLow": "200",
        "wattVoltEnable": "0",
        "caFwEnable": "0",
        "maxOperatingTimeOfGen": "24",
        "micExportGridOff": "0",
        "pvLine": "0",
        "three41": "1",
        "caVwEnable": "0",
        "batteryShutdownVolt": "46",
        "volt3": "14.4",
        "volt4": "28.2",
        "volt1": "6.6",
        "volt2": "10.2",
        "startVoltUp": "1000",
        "volt7": "300",
        "volt8": "300",
        "riso": "0",
        "volt5": "300",
        "volt6": "300",
        "sellTime4Volt": "49",
        "volt9": "300",
        "facLowProtect": "48",
        "wattOverFreq1": "50.2",
        "wattPf4": "11.495",
        "lowNoiseMode": "8000",
        "tempco": "0",
        "arcFactFrz": "-1331091001",
        "wattPf1": "16.061",
        "wattPf2": "11.034",
        "wattPf3": "15.862",
        "meterSelect": "0",
        "genChargeOn": "0",
        "externalCtRatio": "2000",
        "lowThrough": "50",
        "drmEnable": "0",
        "underFreq1Delay": "0.1",
        "gridPeakShaving": "0",
        "fac": "0",
        "vacLowProtect": "185",
        "chargeCurrentLimit": "80",
        "caLv3": "185",
        "sundayOn": "true",
        "batteryImpedance": "8",
        "safetyType": "0",
        "varVolt4": "112.2",
        "varVolt3": "104.3",
        "varVolt2": "95.7",
        "specialFunction": "0",
        "varVolt1": "90.0",
        "mondayOn": "true",
        "commAddr": "0",
        "saturdayOn": "true",
        "dischargeLimit": "0",
        "atsEnable": "0",
        "exMeterCt": "0",
        "overFreq2Delay": "0.1",
        "phase": "0",
        "batteryWorkStatus": "1",
        "genToLoadOn": "0",
        "wattOverWgralFreq": "40",
        "sdBatteryCurrent": "40",
        "underVolt2Delay": "0.1",
        "equChargeTime": "0",
        "gridPeakPower": "8000",
        "reset": "0",
        "vacHighProtect": "265",
        "pwm": "0",
        "highThrough": "115",
        "lockOutVoltVar": "5.0",
        "lockInWattPF": "160.6",
        "caVStart": "250.7",
        "acVoltUp": "130.1",
        "wattFreqEnable": "0",
        "wattOverExitFreq": "50.2",
        "sellTime5Volt": "49",
        "caFStop": "-0.01",
        "lowPowerMode": "0",
        "varVoltEnable": "0",
        "acCoupleFreqUpper": "52",
        "impedanceLow": "0.1",
        "acType": "0",
        "facHighProtect": "51.5",
        "recoveryTime": "60",
        "underVolt2": "185",
        "lithiumMode": "0",
        "underVolt1": "185",
        "gridSignal": "1",
        "wattOverFreq1StartDelay": "0",
        "testCommand": "0",
        "signalIslandModeEnable": "0",
        "upsStandard": "0",
        "reconnMinFreq": "48.2",
        "parallelRegister2": "0",
        "parallelRegister1": "1024",
        "startVoltLow": "300",
        "smartLoadOpenDelay": "100",
        "sellTime1Volt": "49",
        "wattVarActive4": "-212",
        "wattVarActive3": "-254",
        "genConnectGrid": "0",
        "flag2": "0",
        "softStart": "60",
        "lockOutWattPF": "-86.9",
        "sdStartCap": "10",
        "current4": "490",
        "current3": "490",
        "current2": "490",
        "current1": "490",
        "gfdi": "0",
        "current8": "0",
        "current7": "0",
        "current6": "0",
        "current5": "9.5",
        "checkSelfTime": "1",
        "limit": "2",
        "wattW3": "20",
        "wattVarActive2": "-223",
        "wattW4": "20",
        "wattVarActive1": "-241",
        "externalCurrent": "0",
        "wattW1": "100",
        "wattW2": "20",
        "vnResponseTime": "1000",
        "wattUnderExitFreqStopDelay": "0",
        "offset": "1",
        "wattActivePf1": "160",
        "current9": "0",
        "dischargeVolt": "0",
        "qvResponseTime": "1000",
        "wattActivePf4": "-87",
        "wattActivePf2": "-228",
        "four19": "0",
        "wattActivePf3": "277",
        "micExportAll": "0",
        "californiaVoltPressureEnable": "1",
        "equVoltCharge": "57.6",
        "genOffCap": "95",
        "sellTime6Volt": "49",
        "acCoupleOnLoadSideEnable": "0",
        "sdStartVolt": "49",
        "generatorBatteryCurrent": "40",
        "reconnMaxVolt": "263",
        "modbusSn": "1",
        "inverterOutputVoltage": "0",
        "chargeCurrent": "80",
        "solar1WindInputEnable": "0",
        "dcVoltUp": "360",
        "parallel": "0",
        "limter": "0",
        "batErr": "0",
        "backupDelay": "0",
        "dischargeCurrentLimit": "80",
        "arcFactT": "184411967",
        "wattUnderWgalFreq": "40",
        "commBaudRate": "0",
        "equipMode": "0",
        "gridSideINVMeter2": "0",
        "underVolt1Delay": "0.1",
        "arcFaultType": "0",
        "arcFactB": "81186110",
        "normalUpwardSlope": "60",
        "arcFactC": "-1410606851",
        "pf": "1",
        "arcFactD": "-2123320482",
        "genMinSolar": "0",
        "sellTime2Volt": "49",
        "arcFactF": "-279960184",
        "arcFactI": "357260858",
        "acVoltLow": "0",
        "genSignal": "1"
    },
    "success": true
}
```

# Inverter Current Flow Statistics
Request URL: https://api.sunsynk.net/api/v1/inverter/{inverterSerialNumber}/flow

Request Method: GET

Request Headers:
| Header | Value |
| -------- | ------- |
| Authorization | Bearer {TOKEN} |

Expected Response:
```
{
    "code": 0,
    "msg": "Success",
    "data": {
        "custCode": [customerCode],
        "meterCode": 0,
        "pvPower": [currentPvPowerW],
        "battPower": [currentBatterPowerW],
        "gridOrMeterPower": [currentGridPowerW],
        "loadOrEpsPower": [currentLoadPowerW],
        "genPower": 0,
        "minPower": 0,
        "soc": [currentBatterySocPercent],
        "smartLoadPower": 0,
        "upsLoadPower": [currentUpsLoadPowerW],
        "homeLoadPower": [currentHomeLoadPowerW],
        "pvTo": false,        [true when PV is providing power]
        "toLoad": true,       [true when load is present]
        "toSmartLoad": false,
        "toUpsLoad": false,   [true when UPS load is present]
        "toHomeLoad": true,   [true when home load present]
        "toGrid": false,      [true when exporting to grid]
        "toBat": true,        [true when battery charging]
        "batTo": false,       [true when battery discharing]
        "gridTo": true,       [true when importing from grid]
        "genTo": false,       [true when generator is providing power]
        "minTo": false,
        "existsGen": false,   [true when generator exists]
        "existsMin": false,
        "existsGrid": true,   [true when grid exists]
        "genOn": false,       [true when generator is on]
        "microOn": false,
        "existsMeter": false,
        "bmsCommFaultFlag": null,
        "existsThreeLoad": true,
        "existsSmartLoad": false,
        "pv": [
            {
                "power": 0,
                "toInv": false
            },
            {
                "power": 0,
                "toInv": false
            }
        ],
        "existThinkPower": false
    },
    "success": true
}
```

# Inverter Realtime Output
Request URL: https://api.sunsynk.net/api/v1/inverter/{inverterSerialNumber}/realtime/output

Request Method: GET

Request Headers:
| Header | Value |
| -------- | ------- |
| Authorization | Bearer {TOKEN} |

Expected Response:
```
{
    "code": 0,
    "msg": "Success",
    "data": {
        "vip": [
            {
                "volt": "238.6",        -> sunsynk_{inverterSerialNumber}_inverter_voltage
                "current": "9.1",       -> sunsynk_{inverterSerialNumber}_inverter_current
                "power": -2154          -> sunsynk_{inverterSerialNumber}_inverter_power   [negative when pulling power]
            }
        ],
        "pInv": 0,
        "pac": -2154,                   -> sunsynk_{inverterSerialNumber}_inverter_power   [negative when pulling power]
        "fac": 49.9                     -> sunsynk_{inverterSerialNumber}_inverter_frequency
    },
    "success": true
}
```

# Inverter Realtime Input
Request URL: https://api.sunsynk.net/api/v1/inverter/{inverterSerialNumber}/realtime/input

Request Method: GET

Request Headers:
| Header | Value |
| -------- | ------- |
| Authorization | Bearer {TOKEN} |

Expected Response:
```
{
    "code": 0,
    "msg": "Success",
    "data": {
        "pac": 0,
        "grid_tip_power": null,
        "pvIV": [
            {
                "id": null,
                "pvNo": 1,
                "vpv": "1.9",                        -> sunsynk_{inverterSerialNumber}_pv1_voltage
                "ipv": "0.1",                        -> sunsynk_{inverterSerialNumber}_pv1_current
                "ppv": "0.0",                        -> sunsynk_{inverterSerialNumber}_pv1_power
                "todayPv": "0.0",
                "sn": "[inverterSerialNumber]",
                "time": "2025-03-09 00:24:47"
            },
            {
                "id": null,
                "pvNo": 2,
                "vpv": "1.6",                        -> sunsynk_{inverterSerialNumber}_pv2_voltage
                "ipv": "0.0",                        -> sunsynk_{inverterSerialNumber}_pv2_current
                "ppv": "0.0",                        -> sunsynk_{inverterSerialNumber}_pv2_power
                "todayPv": "0.0",
                "sn": "[inverterSerialNumber]",
                "time": "2025-03-09 00:24:47"
            }
        ],
        "mpptIV": [],
        "etoday": 0.00,                              -> sunsynk_{inverterSerialNumber}_day_pv_energy
        "etotal": 0.00                               -> sunsynk_{inverterSerialNumber}_total_pv_energy
    },
    "success": true
}
```

# Inverter Realtime Battery
Request URL: https://api.sunsynk.net/api/v1/inverter/battery/{inverterSerialNumber}/realtime?sn={inverterSerialNumber}&lan=en

Request Method: GET

Request Headers:
| Header | Value |
| -------- | ------- |
| Authorization | Bearer {TOKEN} |

Expected Response:
```
{
    "code": 0,
    "msg": "Success",
    "data": {
        "time": null,
        "etodayChg": "1.0",        -> sunsynk_{inverterSerialNumber}_day_battery_charge
        "etodayDischg": "0.0",     -> sunsynk_{inverterSerialNumber}_day_battery_discharge
        "emonthChg": "78.2",       -> sunsynk_{inverterSerialNumber}_month_battery_charge
        "emonthDischg": "74.4",    -> sunsynk_{inverterSerialNumber}_month_battery_discharge
        "eyearChg": "121.5",       -> sunsynk_{inverterSerialNumber}_year_battery_charge
        "eyearDischg": "113.9",    -> sunsynk_{inverterSerialNumber}_year_battery_discharge
        "etotalChg": "125.7",      -> sunsynk_{inverterSerialNumber}_total_battery_charge
        "etotalDischg": "113.9",   -> sunsynk_{inverterSerialNumber}_total_battery_discharge
        "type": 1,                 -> sunsynk_{inverterSerialNumber}_battery_type [1=Lithium]
        "power": -2016,            -> sunsynk_{inverterSerialNumber}_battery_power [negative when charging]
        "capacity": "315.0",       -> sunsynk_{inverterSerialNumber}_battery_capacity
        "correctCap": 315,
        "bmsSoc": 58.0,
        "bmsVolt": 53.92,
        "bmsCurrent": 36.0,
        "bmsTemp": 16.7,
        "current": -37.3,          -> sunsynk_{inverterSerialNumber}_battery_current [negative when charging]
        "voltage": "54.1",         -> sunsynk_{inverterSerialNumber}_battery_voltage 
        "temp": "16.7",            -> sunsynk_{inverterSerialNumber}_battery_temperature
        "soc": "58.0",             -> sunsynk_{inverterSerialNumber}_battery_soc
        "chargeVolt": 57.6,        -> sunsynk_{inverterSerialNumber}_battery_charge_voltage
        "dischargeVolt": 0.0,      -> sunsynk_{inverterSerialNumber}_battery_discharge_voltage
        "chargeCurrentLimit": 80.0,
        "dischargeCurrentLimit": 80.0,
        "maxChargeCurrentLimit": 0.0,
        "maxDischargeCurrentLimit": 0.0,
        "bms1Version1": 0,
        "bms1Version2": 0,
        "current2": null,
        "voltage2": null,
        "temp2": null,
        "soc2": null,
        "chargeVolt2": null,
        "dischargeVolt2": null,
        "chargeCurrentLimit2": null,
        "dischargeCurrentLimit2": null,
        "maxChargeCurrentLimit2": null,
        "maxDischargeCurrentLimit2": null,
        "bms2Version1": null,
        "bms2Version2": null,
        "status": 1,
        "batterySoc1": 0.0,
        "batteryCurrent1": 0.0,
        "batteryVolt1": 0.0,
        "batteryPower1": 0.0,
        "batteryTemp1": 0.0,
        "batteryStatus2": 0,
        "batterySoc2": null,
        "batteryCurrent2": null,
        "batteryVolt2": null,
        "batteryPower2": null,
        "batteryTemp2": null,
        "numberOfBatteries": null,
        "batt1Factory": null,
        "batt2Factory": null
    },
    "success": true
}
```

# Inverter Realtime Grid
Request URL: https://api.sunsynk.net/api/v1/inverter/grid/{inverterSerialNumber}/realtime?sn={inverterSerialNumber}
Request Method: GET

Request Headers:
| Header | Value |
| -------- | ------- |
| Authorization | Bearer {TOKEN} |

Expected Response:
```
{
    "code": 0,
    "msg": "Success",
    "data": {
        "vip": [
            {
                "volt": "239.2",                                      -> sunsynk_{inverterSerialNumber}_grid_voltage
                "current": "8.7",                                     -> sunsynk_{inverterSerialNumber}_grid_current
                "power": 9767    [Grid Power kW, -ve for export]      -> sunsynk_{inverterSerialNumber}_grid_power
            }
        ],
        "pac": 9767,             
        "qac": 0,
        "fac": 49.96,            [Grid Frequency Hz]                  -> sunsynk_{inverterSerialNumber}_grid_frequency
        "pf": 1.0,
        "status": 1,                                                  -> sunsynk_{inverterSerialNumber}_grid_connected_stratus
        "acRealyStatus": 1,
        "etodayFrom": "4.8",     [Today Import kWh]                   -> sunsynk_{inverterSerialNumber}_day_grid_import
        "etodayTo": "0.0",       [Today Export kWh]                   -> sunsynk_{inverterSerialNumber}_day_grid_export
        "etotalFrom": "287.0",   [Total Import kWh]                   -> sunsynk_{inverterSerialNumber}_total_grid_import
        "etotalTo": "0.0",       [Total Export kWh]                   -> sunsynk_{inverterSerialNumber}_total_grid_export
        "limiterPowerArr": [
            9767,
            0
        ],
        "limiterTotalPower": 9767
    },
    "success": true
}
```

# Inverter Realtime Load
Request URL: https://api.sunsynk.net/api/v1/inverter/load/{inverterSerialNumber}/realtime?sn={inverterSerialNumber}
Request Method: GET

Request Headers:
| Header | Value |
| -------- | ------- |
| Authorization | Bearer {TOKEN} |

Expected Response:
```
{
    "code": 0,
    "msg": "Success",
    "data": {
        "totalUsed": 250.60,                -> sunsynk_{inverterSerialNumber}_total_load_energy
        "dailyUsed": 8.30,                  -> sunsynk_{inverterSerialNumber}_day_load_energy
        "vip": [
            {
                "volt": "245.1",            -> sunsynk_{inverterSerialNumber}_load_voltage
                "current": "0.0",           -> sunsynk_{inverterSerialNumber}_load_current
                "power": 167                -> sunsynk_{inverterSerialNumber}_load_power
            }
        ],
        "totalPower": 167,
        "smartLoadStatus": -1,
        "loadFac": 49.9,                    -> sunsynk_{inverterSerialNumber}_load_frequency
        "upsPowerL1": 0.0,
        "upsPowerL2": 0.0,
        "upsPowerL3": 0.0,
        "upsPowerTotal": 0.0
    },
    "success": true
}
```

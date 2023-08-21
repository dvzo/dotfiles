#!/usr/bin/env python

import sys
import json

"""
takes json object battery as input from eww state
EWW_BATTERY: { <name>: { capacity, status } }

3 statuses:
    1 - Not Charging
    2 - Charging
    3 - Discharging

returns path for correct battery image based on capacity and status
"""

# ewwbattery = json.loads(sys.stdin.read())

ewwbattery = json.loads(sys.stdin.read().replace("EWW_BATTERY: ", ""))
capacity = int(ewwbattery["BAT1"]["capacity"])
status = ewwbattery["BAT1"]["status"]
batteryimagepath = ""

if status == "Charging":
    if capacity >= 0 and capacity < 10:
        batteryimagepath = "images/battery-000-charging.png"

    elif capacity >= 10 and capacity < 20:
        batteryimagepath = "images/battery-010-charging.png"

    elif capacity >= 20 and capacity < 30:
        batteryimagepath = "images/battery-020-charging.png"

    elif capacity >= 30 and capacity < 40:
        batteryimagepath = "images/battery-030-charging.png"

    elif capacity >= 40 and capacity < 50:
        batteryimagepath = "images/battery-040-charging.png"

    elif capacity >= 50 and capacity < 60:
        batteryimagepath = "images/battery-050-charging.png"

    elif capacity >= 60 and capacity < 70:
        batteryimagepath = "images/battery-060-charging.png"

    elif capacity >= 70 and capacity < 80:
        batteryimagepath = "images/battery-070-charging.png"

    elif capacity >= 80 and capacity < 90:
        batteryimagepath = "images/battery-080-charging.png"

    elif capacity >= 90 and capacity < 100:
        batteryimagepath = "images/battery-090-charging.png"

    else:
        batteryimagepath = "images/battery-100-charging.png"
else:
    if capacity >= 0 and capacity < 10:
        batteryimagepath = "images/battery-000.png"

    elif capacity >= 10 and capacity < 20:
        batteryimagepath = "images/battery-010.png"

    elif capacity >= 20 and capacity < 30:
        batteryimagepath = "images/battery-020.png"

    elif capacity >= 30 and capacity < 40:
        batteryimagepath = "images/battery-030.png"

    elif capacity >= 40 and capacity < 50:
        batteryimagepath = "images/battery-040.png"

    elif capacity >= 50 and capacity < 60:
        batteryimagepath = "images/battery-050.png"

    elif capacity >= 60 and capacity < 70:
        batteryimagepath = "images/battery-060.png"

    elif capacity >= 70 and capacity < 80:
        batteryimagepath = "images/battery-070.png"

    elif capacity >= 80 and capacity < 90:
        batteryimagepath = "images/battery-080.png"

    elif capacity >= 90 and capacity < 100:
        batteryimagepath = "images/battery-090.png"

    else:
        batteryimagepath = "images/battery-100.png"

print(batteryimagepath)

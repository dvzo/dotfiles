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
        batteryimagepath = "images/battery-empty-solid-green.png"

    elif capacity >= 10 and capacity < 50:
        batteryimagepath = "images/battery-quarter-solid-green.png"

    elif capacity >= 50 and capacity < 75:
        batteryimagepath = "images/battery-half-solid-green.png"

    elif capacity >= 75 and capacity < 90:
        batteryimagepath = "images/battery-three-quarters-solid-green.png"

    else:
        batteryimagepath = "images/battery-full-solid-green.png"
else:
    if capacity >= 0 and capacity < 10:
        batteryimagepath = "images/battery-empty-solid-red.png"

    elif capacity >= 10 and capacity < 50:
        batteryimagepath = "images/battery-quarter-solid-light.png"

    elif capacity >= 50 and capacity < 75:
        batteryimagepath = "images/battery-half-solid-light.png"

    elif capacity >= 75 and capacity < 90:
        batteryimagepath = "images/battery-three-quarters-solid-light.png"

    else:
        batteryimagepath = "images/battery-full-solid-light.png"

# return a json object for different properties like charing and image path?
battery = {
    "capacity": capacity,
    "status": status,
    "imagepath": batteryimagepath
}

print(json.dumps(battery))

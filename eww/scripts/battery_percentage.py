#!/usr/bin/env python

import sys

"""
this script will read output from $ acpi -b
checks for the battery percentage, and removes last character

$ acpi -b
Battery 0: Not charging, 49%
Battery 0: Discharging, 17%, 00:59:13 remaining
"""

battery_info = sys.stdin.read()
battery_percentage_list = battery_info.split(" ")
battery_percentage = ""

for i in battery_percentage_list:
    if "%" in i:
        battery_percentage = i

if battery_percentage[-1] != "%":
    battery_percentage = battery_percentage[0:-1]

print (battery_percentage)

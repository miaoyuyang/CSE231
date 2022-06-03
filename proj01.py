#!/usr/bin/env python3
# -*- coding: utf-8 -*-

num_str = input( "Input rods: " )
num_float = float( num_str )

meters = float( num_str ) * 5.0292
feet = meters / 0.3048
miles = meters / 1609.34
furlongs = float( num_str ) / 40
rods = round(miles/(3.1/60),3)

print("You input", num_float, "rods.")
print("")
print("Conversions")
print("Meters:", round(meters,3))
print("Feet:", round(feet,3))
print("Miles:", round(miles,3))
print ("Furlongs:", round(furlongs,3))
print("Minutes to walk", num_float, "rods:",rods)
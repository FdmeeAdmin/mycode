#!/usr/bin/env python3
# create a list of strings
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# loop across the list called vendors
for x in farms:
    print("\nThe vendor is " + x, end="")   # newline, print current vendor, and end without newline
    if x in farms: 
        print(" - NOT AN APPROVED FARMS!", end="")
print("\nOur loop has ended.") # print when loop has finished


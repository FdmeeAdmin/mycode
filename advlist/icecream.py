#!/usr/bin/env python3
icecream=["flavors", "salty"]
print(icecream)
num=99
icecream.append(num)
print(icecream)
# input for a user's name
name= input("What is your name? ")

# print that put all of that together
print(f"{icecream[-1]} {icecream[0]} and {name} chooses to be {icecream[1]}")

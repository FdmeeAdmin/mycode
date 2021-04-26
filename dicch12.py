#!/usr/bin/env python3
switch={"hostname": "sw1", "ip": "11.1.1.1", "version": "1.2", "Vendor": "cisco"}

print( switch["hostname"] )
print( switch["ip"] )

print( "First test - .get()")
print( switch.get("lynx") )

print( "second test - .get()")
print( switch.get("lynx", "THE KEY IS IN ANOTHER CASTLE!") )

print( "Third test - .get()")
print( switch.get("version") )

print( "Fourth test - .keys()" )
print( switch.values())

print( "fifth test - .values()" )
print( switch.values() )

print( "Sixth test - .pop()")
switch.pop("version")
print( switch.keys() )
print( switch.values() )

print( "Seventh test - ADD a new value" )
switch["adminlogin"] = "karlo8"
print( switch.keys() )
print( switch.values() )

print( "Eight test - ADD a new value" )
switch["password"] = "qwerty"
print( switch.keys() )
print ( switch.values() )


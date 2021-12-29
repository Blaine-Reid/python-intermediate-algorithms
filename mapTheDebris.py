# Intermediate Algorithm Scripting: Map the Debris
# Return a new array that transforms the elements' average altitude into their orbital periods (in seconds). 
# The array will contain objects in the format {name: 'name', avgAlt: avgAlt}. The values should be rounded to 
# the nearest whole number. The body being orbited is Earth. The radius of the earth is 6367.4447 kilometers, 
# and the GM value of earth is 398600.4418 km3s-2.

import math

def orbitalPeriod(arr):
    '''Calculates the orbital period of celestial objects.'''
 
    gm = 398600.4418
    earthRadius = 6367.4447
    print([dict([
                ("name",x['name']),
                ("orbitalPeriod",round((2*math.pi)*math.sqrt((math.pow(x['avgAlt']+earthRadius,3))/gm)))
                ])
                for x in arr 
                ])
        

orbitalPeriod([{"name" : "sputnik", "avgAlt" : 35873.5553}]) 
#should return [{name: "sputnik", orbitalPeriod: 86400}].
orbitalPeriod([{"name": "iss", "avgAlt": 413.6}, {"name": "hubble", "avgAlt": 556.7}, {"name": "moon", "avgAlt": 378632.553}]) 
#should return [{name : "iss", orbitalPeriod: 5557}, {name: "hubble", orbitalPeriod: 5734}, {name: "moon", orbitalPeriod: 2377399}].
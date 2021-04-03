# Truck Tour

from collections import deque

n = int(input())
gas_stations = []
tank_capacity = 0
valid = True

for _ in range(n):
    gas_stations.append(input())  # 1st num is the amount of petrol # 2nd num is the distance to next station

que = deque(gas_stations)  # making possible to pop/append from BOTH sides of the list now.

for index in range(n):
    for el in que:
        petrol, distance = el.split()
        petrol = int(petrol)
        distance = int(distance)
        tank_capacity += petrol
        if tank_capacity >= distance:
            tank_capacity -= distance
        elif tank_capacity < distance:
            tank_capacity = 0
            que.rotate(-1)  # current station goes last, next station becomes 1st later
            valid = False
            break
    if valid:
        print(index)
        break
    else:
        valid = True

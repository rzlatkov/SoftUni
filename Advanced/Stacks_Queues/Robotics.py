# Robotics

from collections import deque
from datetime import datetime, timedelta

inpt = input().split(';')
time = datetime.strptime(input(), '%H:%M:%S')

robots = []
available_robots = []
products = []

for el in inpt:
    data = el.split('-')
    robot = {}
    robot['name'] = data[0]
    robot['processing_time'] = int(data[1])
    robot['available_at'] = time
    robots.append(robot)
    available_robots.append(robot)

command = input()

while command != "End":
    products.append(command)
    command = input()

products = deque(products)
available_robots = deque(available_robots)

time = time + timedelta(seconds=1)

while len(products) > 0:

    current_product = products.popleft()

    if available_robots:
        current_robot = available_robots.popleft()
        current_robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
        robot = [el for el in robots if el == current_robot][0]
        robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
        print(f"{robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    else:
        for rob in robots:
            if time >= rob['available_at']:
                available_robots.append(rob)
        if not available_robots:
            products.append(current_product)
        else:
            current_robot = available_robots.popleft()
            print(f"{current_robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
            current_robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
            robot = [el for el in robots if el == current_robot][0]
            robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])

    time = time + timedelta(seconds=1)

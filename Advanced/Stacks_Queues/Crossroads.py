# Crossroads

from collections import deque

duration = int(input())
window = int(input())

cars = deque()
counter = 0
crash = False

command = input()

while command != "END":
    if command == 'green':
        if cars:
            current_car = cars.popleft()
            time_left = duration - len(current_car)
            while time_left > 0:
                counter += 1
                if cars:
                    current_car = cars.popleft()
                    time_left -= len(current_car)
                else:
                    break
            if time_left == 0:
                counter += 1
            if window >= abs(time_left):
                if time_left < 0:
                    counter += 1
            else:
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[window + time_left]}.")
                crash = True
                break
    else:
        cars.append(command)
    command = input()

if not crash:
    print("Everyone is safe.")
    print(f"{counter} total cars passed the crossroads.")

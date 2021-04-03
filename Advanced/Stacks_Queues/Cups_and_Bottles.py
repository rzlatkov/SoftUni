# Cups and bottles

from collections import deque

cups = [int(cup) for cup in input().split()]
bottles = [int(bottle) for bottle in input().split()]
cups = deque(cups)
wasted_water = 0
managed = False

while len(bottles) > 0:
    if cups:
        current_cup = cups.popleft()
        current_bottle = bottles.pop()
        difference = current_bottle - current_cup
        if difference == 0:
            pass
        elif difference > 0:
            wasted_water += difference
        elif difference < 0:
            cups.appendleft(abs(difference))
        if not cups:
            managed = True
            break
    else:
        managed = True
        break

if managed:
    modified = [str(el) for el in bottles]
    print(f"Bottles: {' '.join(modified)}")
    print(f"Wasted litters of water: {wasted_water}")
else:
    modified = [str(el) for el in cups]
    print(f"Cups: {' '.join(modified)}")
    print(f"Wasted litters of water: {wasted_water}")

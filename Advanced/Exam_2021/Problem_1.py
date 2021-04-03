# 2021 problem 1

from collections import deque

firework_effects = [int(f) for f in input().split(', ') if int(f) > 0]
explosive_power = [int(ex) for ex in input().split(', ') if int(ex) > 0]

firework_effects = deque(firework_effects)

palm_count = 0
willow_count = 0
crossette_count = 0

success = False

while len(firework_effects) > 0:
    if explosive_power:
        current_firework = firework_effects.popleft()
        current_explosive = explosive_power.pop()

        sum = current_explosive + current_firework

        if sum % 3 == 0 and sum % 5 != 0:
            palm_count += 1
        elif sum % 5 == 0 and sum % 3 != 0:
            willow_count += 1
        elif sum % 5 == 0 and sum % 3 == 0:
            crossette_count += 1
        else:
            current_firework -= 1
            if current_firework > 0:
                firework_effects.append(current_firework)
            explosive_power.append(current_explosive)

        if palm_count >= 3 and willow_count >= 3 and crossette_count >= 3:
            # success = True
            break
    else:
        break

if palm_count >= 3 and willow_count >= 3 and crossette_count >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can’t make the perfect firework show.")

if firework_effects:
    modified = [str(el) for el in firework_effects]
    print(f"Firework Effects left: {', '.join(modified)}")

if explosive_power:
    modified = [str(el) for el in explosive_power]
    print(f"Explosive Power left: {', '.join(modified)}")

print(f"Palm Fireworks: {palm_count}")
print(f"Willow Fireworks: {willow_count}")
print(f"Crossette Fireworks: {crossette_count}")

# input 1
# -15, -8, 0, -16, 0, -22
# 10, 5

# input 2

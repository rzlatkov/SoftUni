# Bombs

from collections import deque

bomb_effects = input().split(', ')
bomb_casings = input().split(', ')

bomb_effects = deque(bomb_effects)

datura_count = 0
cherry_count = 0
smoke_count = 0

bene = False

while len(bomb_casings) > 0:
    if bomb_effects:
        current_effect = int(bomb_effects.popleft())
        current_casing = int(bomb_casings.pop())
        if current_effect + current_casing == 40:
            datura_count += 1
        elif current_effect + current_casing == 60:
            cherry_count += 1
        elif current_effect + current_casing == 120:
            smoke_count += 1
        else:
            bomb_casings.append(str(current_casing - 5))
            bomb_effects.appendleft(str(current_effect))

        if datura_count >= 3 and cherry_count >= 3 and smoke_count >= 3:
            bene = True
            break
    else:
        break

if bene:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(bomb_effects)}")

if not bomb_casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(bomb_casings)}")

print(f"Cherry Bombs: {cherry_count}")
print(f"Datura Bombs: {datura_count}")
print(f"Smoke Decoy Bombs: {smoke_count}")

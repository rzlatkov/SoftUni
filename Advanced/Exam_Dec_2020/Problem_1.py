from collections import deque

males = [int(m) for m in input().split()]
females = [int(fm) for fm in input().split()]

females = deque(females)

matches = 0

while len(males) > 0:
    if females:
        current_male = males.pop()
        current_female = females.popleft()

        if current_male % 25 == 0 and current_male != 0:
            females.appendleft(current_female)
            if len(males) == 0:
                break
            current_male = males.pop()
            continue

        if current_female % 25 == 0 and current_female != 0:
            males.append(current_male)
            if len(females) == 0:
                break
            current_female = females.popleft()
            continue

        if current_male <= 0:
            females.appendleft(current_female)
            continue
        if current_female <= 0:
            males.append(current_male)
            continue

        if current_male != current_female:
            if current_male - 2 > 0:
                males.append(current_male - 2)
        else:
            matches += 1
    else:
        break

print(f"Matches: {matches}")

if males:
    males.reverse()
    modified = [str(male) for male in males]
    print(f"Males left: {', '.join(modified)}")
else:
    print(f"Males left: none")

if females:
    modified = [str(fm) for fm in females]
    print(f"Females left: {', '.join(modified)}")
else:
    print(f"Females left: none")

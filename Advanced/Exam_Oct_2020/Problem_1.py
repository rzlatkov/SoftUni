from collections import deque

jobs = [int(j) for j in input().split(', ')]
index = int(input())
wanted_job = jobs[index]
cycles = 0
counter = 0

occurence = jobs[:index+1].count(wanted_job)

jobs.sort()
jobs = deque(jobs)

while len(jobs) > 0:
    current = jobs.popleft()
    cycles += current
    if current == wanted_job:
        counter += 1
        if counter == occurence:
            break

print(cycles)

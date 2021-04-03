# Longest Intersection

lines_count = int(input())
longest_combo = ()
max_len = 0

for _ in range(lines_count):
    ranges = input().split('-')
    start1, end1 = ranges[0].split(',')
    start2, end2 = ranges[1].split(',')
    result_len = min(int(end1), int(end2)) - max(int(start1), int(start2)) + 1
    if result_len > max_len:
        max_len = result_len
        longest_combo = (max(int(start1), int(start2)), min(int(end1), int(end2)))

result = []
for i in range(longest_combo[0], longest_combo[1] + 1):
    result.append(i)

print(f"Longest intersection is {result} with length {len(result)}")

n = int(input())
s = list(map(int, input().split()))
location = {}
r = float('inf')
for idx, i in enumerate(s):
    if i not in location:
        location[i] = []
        location[i].append(idx)
        continue
    location[i].append(idx)
    r = min(r, abs(location[i][-2] - location[i][-1]) + 1)

print(r if r != float('inf') else -1)
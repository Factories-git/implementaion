from collections import defaultdict

n, q = map(int, input().split())
pigeon_loc = defaultdict(set)
for i in range(1, n+1):
    pigeon_loc[i].add(i)

for _ in range(q):
    s = input().split()
    if s[0] == '3':
        print(pigeon_loc[int(s[1])])
        continue
    c, a, b = map(int, s)
    if c == 1:
        pigeon[pigeon_loc[a] - 1].remove(a)
        pigeon_loc[a] = b
        pigeon[pigeon_loc[b]-1].add(a)
    elif c == 2:
        pigeon[a-1], pigeon[b-1] = pigeon[b-1], pigeon[a-1]
        print(pigeon_loc, pigeon)
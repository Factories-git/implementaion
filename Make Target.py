n = int(input())
s = [['?'] * n for _ in range(n)]
for i in range(n):
    j = n+1-i-1
    if i > j:
        continue
    for a in range(i, j):
        for b in range(i, j):
            s[a][b] = '#' if not i % 2 else '.'
for i in s:
    print(''.join(i))

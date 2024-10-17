n,m = map(int, input().split())
s,d = divmod(n,m)
print(s)
print(d if d != 0 else 0)
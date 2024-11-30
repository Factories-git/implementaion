r,c = map(int,input().split())
for i in range(1,r+1):
    s = input()
    if i % 2 == 0:
        if c-len(s) % 2 == 0:
            s = s.rjust((c-len(s)), '.')
        else:
            s = s.rjust(c-len(s)-1, '.')
        s += s.ljust(c-len(s), '.')
    else:
        if c-len(s) % 2 == 0:
            s = s.ljust((c-len(s)), '.')
        else:
            s = s.ljust(c-len(s)-1, '.')
        s += s.rjust(c-len(s), '.')
    print(s)
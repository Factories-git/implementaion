taka, aoki = input().split()
if taka == 'sick':
    if aoki == 'sick':
        print(1)
        exit(0)
    else:
        print(2)
        exit(0)
elif aoki == 'sick':
    if taka == 'fine':
        print(3)
        exit(0)
else:
    print(4)
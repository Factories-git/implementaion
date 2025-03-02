n = int(input())
s = list(map(int, input().split()))
for i in range(n-1):
    if not s[i] < s[i+1]:
        print('No')
        exit(0)
print('Yes')
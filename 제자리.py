# import random
#
# n = random.randint(1,250000)
# l = list(random.randint(1,n)for i in range(n))
# cnt = 0
# d = 0
# pass_set = set()
# if n == 1:
#     print(0)
#     exit(0)
# for i in range(len(l)):
#     if l[i] != i-d:
#         cnt += 1
#         if i != 0:
#             d += 1
# print(n)
# print(cnt if cnt != 0 else n)

n = int(input())
l = list(map(int, input().split()))
cnt = 0
d = 1
for i in range(len(l)):
    if l[i] == d:
        d += 1
        continue
    cnt += 1
print(cnt)
n,m = map(int, input().split())
fish_shaped_bread = [list(input()) for _ in range(n)]
for i in range(n):
    fish_shaped_bread[i] = fish_shaped_bread[i][::-1]
    print(''.join(fish_shaped_bread[i]))
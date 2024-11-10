n = int(input())
card = list(map(int, input().split()))
point = 0
fir = card[0]
pre = card[0]

for i in card[1:]:
    if i != pre + 1:
        point += fir
        fir = i
    pre = i

point += fir
print(point)
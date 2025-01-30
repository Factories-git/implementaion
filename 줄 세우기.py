n = int(input())
picked = list(map(int, input().split()))
students = [i for i in range(1, n+1)]
for i in range(1, n):
    if picked[i] == 0:
        continue
    students.insert(i-picked[i], students.pop(i))

print(*students)
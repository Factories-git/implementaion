import sys

input = sys.stdin.readline

n = int(input())
sys.stdout.flush()
sign_by_mul = {}
signs = [''] * (n+1)
bonus = False

is_n1 = 0
is_n2 = 0
for i in range(2, n+1):
    print(f"? {i-1} * {i}")
    sys.stdout.flush()
    res = input().strip()
    sign_by_mul[f"{i-1}*{i}"] = res
    if res == '+' and not bonus:
        print(f"? {i-1} + {i}")
        sys.stdout.flush()
        res = input().strip()
        if res == '+':
            signs[i-1] = '+'
            signs[i] = '+'
        else:
            signs[i-1] = '-'
            signs[i] = '-'
        is_n1 = i-1
        is_n2 = i
        bonus = True

for expression, recep in sign_by_mul.items():
    n1, n2 = expression.split('*')
    n1, n2 = int(n1), int(n2)
    if n2 == is_n1:
        if recep == '-':
            signs[n1] = '+' if signs[n2] == '-' else '-'
        else:
            signs[n1] = signs[n2]
    elif n1 == is_n2:
        if recep == '-':
            signs[n2] = '+' if signs[n1] == '-' else '-'
        else:
            signs[n2] = signs[n1]

for i in range(n-1, 1, -1):
    if signs[i-1] != '' and signs[i] != '':
        continue
    result = sign_by_mul[f'{i-1}*{i}']
    if signs[i-1] == '':
        if result == '+':
            signs[i-1] = signs[i]
        else:
            signs[i-1] = '+' if signs[i] == '-' else '-'
    if signs[i] == '':
        if result == '+':
            signs[i] = signs[i-1]
        else:
            signs[i] = '+' if signs[i-1] == '-' else '-'
print('!', ' '.join(signs[1:]))
sys.stdout.flush()
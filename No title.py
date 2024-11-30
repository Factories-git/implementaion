import sys

input = sys.stdin.readline

n = int(input())
sys.stdout.flush()
signs = [''] * (n+1)
print('? 1 * 2')
sys.stdout.flush()
res = input().strip()
if res == '+':
    signs[1] = '+'
else:
    signs[1] = '-'
for i in range(2,n+1):
    print(f'? {i-1} * {i}')
    sys.stdout.flush()
    res = input().strip()
    if res == '+':
        signs[i] = signs[i-1]
    else:
        signs[i] = '-' if signs[i-1] == '+' else '+'
result = ' '.join(signs[1:])
print(f"! {result}")
sys.stdout.flush()

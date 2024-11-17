from collections import deque
import sys

input = sys.stdin.readline
back = deque()
front = deque()
now = 0


def backward():
    global now
    if len(back) == 0:
        return
    front.append(now)
    now = back.pop()


def frontward():
    global now
    if len(front) == 0:
        return
    back.append(now)
    now = front.pop()



def visit(a):
    global now_cash, back, front, now
    while front:
        now_cash -= cash[front.pop()-1]
    if now != 0:
        back.append(now)
    now = a
    while back and now_cash + cash[a-1] > c:
        s = back.popleft()
        now_cash -= cash[s-1]
    now_cash += cash[now-1]


def compression():
    global now_cash
    s = deque()
    pre = -1
    while back:
        c = back.popleft()
        if c != pre:
            s.append(c)
            pre = c
        else:
            now_cash -= cash[c-1]

    return s


n,q,c = map(int, input().split())
cash = list(map(int, input().split()))
now_cash = 0
for i in range(q):
    s = input().split()
    if s[0] == 'B':
        backward()
    elif s[0] == 'F':
        frontward()
    elif s[0] == 'A':
        visit(int(s[1]))
    else:
        back = compression()

print(now)
if back:
    print(*reversed(back))
else:
    print(-1)
if front:
    print(*reversed(front))
else:
    print(-1)
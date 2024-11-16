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
    global back, front, now
    if now != 0:
        back.append(now)
    now = a
    front = deque()


def compression():
    back.appendleft(0)
    s = deque()
    pre = 0
    for i in range(len(back)):
        if back[i] != back[pre]:
            s.append(back[i])
        pre = i
    back.popleft()
    return s


n,q = map(int, input().split())
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
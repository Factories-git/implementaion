'''
맨 끝의 print 빼고는 실행이 잘 되는 지를 보기 위한 용도입니다.
'''

from collections import deque

n, k = map(int, input().split())
conveyor = deque(map(int, input().split()))
stage = 0
robot = deque([0] * n * 2)
pass_ = set()

def is_finish():
    if conveyor.count(0) >= k:
        return True
    return False

def clear_():
    for i in range(n-1,len(robot)):
        robot[i] = 0

while True:
    stage += 1  # 단계 상승
    #1번 행동
    # 컨베이어 벨트 회전
    conveyor.appendleft(conveyor.pop())
    #로봇도 회전
    robot.appendleft(robot.pop())
    print(1,robot, conveyor)
    #회전 했으니 로봇들의 좌표 상승
    clear_() #로봇 내리기
    for i in range(n-1):
        if i not in pass_:
            if robot[i] == 1:
                print(i)
                if robot[i+1] == 0 and conveyor[i+1] >= 1:
                    robot[i+1],robot[i] = robot[i], robot[i+1]
                    conveyor[i+1] -= 1
                    pass_.add(i+1)
    print(2,robot, conveyor)
    clear_()
    #새로운 로봇을 올림
    if conveyor[0] > 0:  #만약 올리는 위치에 올릴 수 있다면
        conveyor[0] -= 1  #내구도 하락
        robot[0] = 1
    print(3,robot, conveyor)
    if is_finish():  #만약 0의 개수가 k개 이상이면
        break  #종료

print(stage)

'''
맨 끝의 print 빼고는 실행이 잘 되는 지를 보기 위한 용도입니다.
'''

from collections import deque

n, k = map(int, input().split())
conveyor = deque(map(int, input().split()))
stage = 0
robot = []


def is_finish():
    if conveyor.count(0) >= k:
        return True
    return False


while True:
    stage += 1 # 단계 상승
    #1번 행동
    # 컨베이어 벨트 회전
    conveyor.appendleft(conveyor.pop())
    #회전 했으니 로봇들의 좌표 상승
    for i in range(len(robot)):
        robot[i] += 1

    print(conveyor, robot)
    #2번 행동
    # 만약 로봇이 하나라도 있으면
    if robot:
        for i in range(n): #n번 반복
            if i in robot: #지금 위치가 로봇이 있는 위치라면
                #이동할 수 있는 지 확인.
                if i + 1 not in robot and conveyor[i + 1] >= 1:
                    conveyor[i + 1] -= 1 #이동 했으니 내구도 하락
    #로봇 위치 상승
    for i in range(len(robot)):
        robot[i] += 1

    print(conveyor, robot)
    #새로운 로봇을 올림
    if conveyor[0] != 0: #만약 올리는 위치에 올릴 수 있다면
        conveyor[0] -= 1 #내구도 하락
        robot.append(0) #로봇의 좌표 추가
    print(conveyor, robot)
    if is_finish(): #만약 0의 개수가 k개 이상이면
        break #종료

print(stage)

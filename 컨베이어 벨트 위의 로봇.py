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
    for i in range(n-1, len(robot)):
        robot[i] = 0


while True:
    stage += 1  # 단계 상승

    #1번 행동
    # 컨베이어 벨트 회전
    temp = conveyor[len(conveyor) - 1]
    for i in range(len(conveyor) - 1, 0, -1):
        conveyor[i] = conveyor[i - 1]
    conveyor[0] = temp
    #로봇도 회전
    temp = robot[len(robot) - 1]
    for i in range(len(robot) - 1, 0, -1):
        robot[i] = robot[i - 1]
    robot[0] = temp

    clear_()
    #회전 했으니 로봇들의 좌표 상승

    for i in range(n-1,-1,-1):
        if robot[i] == 1:
            if robot[i+1] == 0 and conveyor[i+1] >= 1:
                robot[i+1],robot[i] = robot[i], robot[i+1]
                conveyor[i+1] -= 1
    clear_()


    #새로운 로봇을 올림
    if conveyor[0] != 0:  #만약 올리는 위치에 올릴 수 있다면
        conveyor[0] -= 1  #내구도 하락
        robot[0] = 1
    if is_finish():  #만약 0의 개수가 k개 이상이면
        break  #종료
print(stage)
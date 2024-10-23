king, stone, n = map(str, input().split())
chess = [[0] * 8 for _ in range(8)]
king = [8 - int(king[1]), ord(king[0].lower()) - 97]
stone = [8 - int(stone[1]), ord(stone[0].lower()) - 97]
stone[1] = int(stone[1])
king[1] = int(king[1])
chess[king[0]][king[1]] = 1
chess[stone[0]][stone[1]] = 2
for i in range(int(n)):
    d = list(input())
    for direction in d:
        if direction == 'R':
            if king[1] + 1 > 7 or stone[1] + 1 > 7:
                break
            chess[king[0]][king[1]] = 0
            chess[king[0]][king[1] + 1] = 1
            king[1] += 1
            chess[stone[0]][stone[1]] = 0
            chess[stone[0]][stone[1] + 1] = 1
            stone[1] += 1

        elif direction == 'L':
            if king[1] - 1 <= -1 or stone[1] - 1 <= -1:
                break
            chess[king[0]][king[1]] = 0
            chess[king[0]][king[1] - 1] = 1
            king[1] -= 1
            chess[stone[0]][stone[1]] = 0
            chess[stone[0]][stone[1] - 1] = 1
            stone[1] -= 1

        elif direction == 'B':
            if king[0] + 1 > 7 or king[0] + 1 > 7:
                break
            chess[king[0]][king[1]] = 0
            chess[king[0] + 1][king[1]] = 1
            king[0] += 1
            chess[stone[0]][stone[1]] = 0
            chess[stone[0] + 1][stone[1]] = 1
            stone[0] += 1

        elif direction == 'T':
            if king[0] - 1 < 0 or king[0] - 1 < 0:
                break
            chess[king[0]][king[1]] = 0
            chess[king[0] - 1][king[1]] = 1
            king[0] -= 1
            chess[stone[0]][stone[1]] = 0
            chess[stone[0] - 1][stone[1]] = 1
            stone[0] -= 1
    print(d, direction)
print(king, stone)
print(f'{chr(king[0] + 97)}{int(king[1]) + 1} {chr(stone[0] + 97)}{int(stone[1]) + 1}')

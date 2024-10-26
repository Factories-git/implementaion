score = []
for i in range(6):
    score.append(int(input()))
score2 = score[-2:]
score = score[:-2]
score.sort(reverse=True)
score2.sort(reverse=True)
print(score[0] + score[1] + score[2] + score2[0])
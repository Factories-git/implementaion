def solution(n, arr1, arr2):
    answer = []
    cipher_1 = []
    cipher_2 = []
    for i in arr1:
        bined = bin(i)[2:]
        if len(bined) < n:
            bined = '0' * (n - len(bined)) + bined
        cipher_1.append(bined)
    for i in arr2:
        bined = bin(i)[2:]
        if len(bined) < n:
            bined = '0' * (n - len(bined)) + bined
        cipher_2.append(bined)

    for k, r in zip(cipher_1, cipher_2):
        s = ''
        for i, j in zip(k, r):
            if i == '1':
                s += '#'
            elif j == '1':
                s += '#'
            else:
                s += ' '
        answer.append(s)
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
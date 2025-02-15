def solution(s):
    zero = 0
    count = 0
    while s != '1':
        count += 1
        minus = s.count('0')
        zero += minus
        length = len(s) - minus
        s = format(bin(length)[2:])
    return [count, zero]

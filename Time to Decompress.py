import sys

for i in range(int(input())):
    how,word = map(str,sys.stdin.readline().split())
    print(int(how) * word)
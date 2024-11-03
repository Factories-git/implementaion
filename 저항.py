dic = {'black' : 0, 'brown' : 1, 'red' : 2, 'orange' : 3 , 'yellow' : 4, 'green' : 5, 'blue' : 6
    , 'violet' :  7, 'grey' : 8, 'white' : 9}

r = ''
f = input()
s = input()
t = input()

print((dic[f] * 10 + dic[s]) * 10**dic[t])
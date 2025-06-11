# while True:
#     a,b = map(int,input().split())
#     if a == 0 and b == 0 :
#         break
#     else :
#         print (a + b)



import sys

# a, b = map(int,input().split())
a, b = mapt(int, sys.stdin.readline().split())


try :
    while True:
        if a == ' ' and b ==' ':
            break
        else:
            print(a + b)

except EOFError:
    break
--

import sys 
try :
    while True:
        a, b = map (int, sys.stdin.readline().split())
        print(a + b)

except :
    pass
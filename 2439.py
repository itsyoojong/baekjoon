n = int(input())

for i in range(1,n+1):
    # print (f"{*}*{i.rjust()}")   #{} = 변수 
    print(('*' * i).rjust())

-

    n = int(input())

for i in range(1, n + 1):
    print(('*' * i).rjust(n))

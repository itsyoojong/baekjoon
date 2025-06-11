t = int(input())
a, b = map(int,input().split())

for i in range(t):
    print(f"Case#{i}: a + b = {a+b} ")



t = int(input())

for i in range(t):  #t값 하나씩 나옃
    a, b = map(int,input().split())
    print(f"Case # {i+1}: {a} + {b} = {a + b}")
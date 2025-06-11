최초코드
t = int(input())

for _ in range(t)
    a,b = map(int,input().split())
    print('Case#'range(1:t),a+b)

개선된 코드 
t = int (input())
for i in range(t):
    a,b = map(int,input().split())
    print('Case#'i':'a+b)

    print(f"case{i+1}: {a + b}")



--

t = int(input())

for i in range(t):
    a, b = map(int,input().split())
    print(f"Case # {i + 1}: {a + b}")
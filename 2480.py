
# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.

a,b,c = map(int,input().split())
num = sorted([a,b,c])

if a == b == c :
    coin = 10000+ a * 1000
elif a == b or a == c :
    coin = 1000 + a * 100
elif b == c :
    coin = 1000 + b * 100
else :
    coin = max (a,b,c) * 100

print (coin)

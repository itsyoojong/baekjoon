# 준원이는 저번 주에 살면서 처음으로 코스트코를 가 봤다. 정말 멋졌다. 
# 그런데, 몇 개 담지도 않았는데 수상하게 높은 금액이 나오는 것이다! 
# 준원이는 영수증을 보면서 정확하게 계산된 것이 맞는지 확인해보려 한다.

# 영수증에 적힌,

# 구매한 각 물건의 가격과 개수
# 구매한 물건들의 총 금액
# 을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 
# 영수증에 적힌 총 금액과 일치하는지 검사해보자.


# 첫째 줄에는 영수증에 적힌 총 금액 
# X가 주어진다.

# 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 
# N이 주어진다.

# 이후 
# N개의 줄에 각 물건의 가격 a와 
# 개수 b가 공백을 사이에 두고 주어진다.

# 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 
# 일치하면 Yes를 출력한다. 일치하지 않는다면 No를 출력한다.

# 최초 작성
# toprice = int(input())
# numbers = int(input())

# while True:
#     a, b = map(int,input().split())
#     if a,b == '':
#         break
# atotal = sum(a)
# btotal = sum(b)
# if atotal == toprice :
#     print('Yes')
# else :
#    print('No') 
# ==================
# 개선된 코드를 바탕으로 고민한 코드 

toprice = int(input())
n = int(input())

sprice = 0 

for _ in range(n):
    a, b = map (int,input().split())

    sprice += a * b

if sprice == toprice:
    print("Yes")

else :
    print ("No")


# 개선된 코드

# toprice = int(input()) #총 금액
# numbers = int(input()) #항목 개수

# sum_total = 0 

# for _ in range(numbers):
#     a, b = map(int,input().split())
#     sum_total += a * b  # sumtotal에 실제 총 가격 반환

# if sum_total == toprice:
#     print ('Yes')

# else :
#     print ('No')
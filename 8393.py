# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

# 1부터 n까지 합을 출력한다.

# 최초 코드
n = int(input())
a = list(range(1,n).split())



print(sum(a))

# 개선된것 
n = int(input())
a = list(range(1, n+1))
print(sum(a))

# 더 개선된 것
n = int(input())
print(sum(range(1, n+1)))

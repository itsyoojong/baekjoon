# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.

# 최초 풀이 
# a = int(input())
# b = list(range(1, 10))

# for numbers in b :
#     print (a '*' numbers)



a = int(input())
b = list(range(1, 10))

for numbers in b :
    print (f"{a} * {numbers} = {a * numbers}")

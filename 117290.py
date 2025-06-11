# n = int(input())
# tot = 0 

# for i in range(1,n+1): # 1에서 n+1까지의 수를 i 에 반환 
#     tot = tot + i 

# print (tot)

# 문제 이해를 잘못함 첫번째 줄에 n이 주어지고 n까지의 합계인줄.


a = int(input())
b = input().strip()
tot = 0

try :
    a == b 
    
    for i in b :
        tot += i
print (tot)
    
except :
    print('value error')
    
    
    
    # ---

a = int(input())    #입력문 받기
b = input().strip() #불필요한 공백제거
tot = 0             #0으로 설정

try :
    if len(b) != a: # 숫자 나열문의 길이가 a와 다르다면
        raise ValueError #value error로 간주
    for i in b :         # 숫자나열문을 i에 하나씩 반환 
        tot += int(i)    # 반환된 것들을 tot에 더해서 저장
        
    print (tot)          # 총합을 프린트

except:
    pass    #break가 아닌 pass break는 for 이나 while에서만 쓸수 잇다.
            #이외의 중단의 경우 메세지출력하고 종료시키거나 return으로 빠져나갈 수 있다.
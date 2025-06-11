
n = int(input())

for _ in range(n//4):
	print('long'.rstrip())      #rstrip 말고 공백 포함해서 붙여줘야함
    

print (  “int”)
	   


n = int(input())            # n에 정수로 입력받음

for _ in range(n // 4):     # n을 4로 나눈 수만큼 아래 행위 반복할거
    print("long", end=' ')  # long 끝에 공백 추가 

print("int")                # 끝에 int 출력

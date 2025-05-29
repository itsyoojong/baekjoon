# 첫째 줄에는 현재 시각이 나온다. 
# 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다. 
# 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다.



# nowh,nowm = map(int,input().split())
# needh,needm = map(int,input().split())
# h = nowh + needh
# m = nowm + needm
# if m >= 60:
#     h += 1

# print (h,m)
# --------------------

nowh, nowm =map(int, input().split())
needm = int(input())

nowm += needm
nowh += nowm // 60 
nowm = nowm % 60
nowh = nowh % 24
print (nowh,nowm)

# ---
# if needm >= 60:
#     nowh += needm /60 
#     nowm += needm % 60 
# else:
#     nowm + needm >= 60: 
#     nowh += needm /60 
#     nowm += needm % 60 

#     ==================
# nowh, nowm = map(int, input().split())  # 현재 시와 분
# cook = int(input())                     # 요리 시간 (분 단위)

# # 분 더하기
# nowm += cook

# # 시 보정
# nowh += nowm // 60
# nowm = nowm % 60

# # 시가 24시 이상이면 0~23으로 돌림
# nowh = nowh % 24

# print(nowh, nowm)

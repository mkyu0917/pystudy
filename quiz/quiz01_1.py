str = "Life is short, You need Python"


str=str.lower() # 소문자 변경
str=str.replace(" ","") # 공백 제거
str=str.replace(",","") # 컴마 제거

print("소문자 출력: ",str)
print("총 갯수:",len(str))

lst = list(str) # str을 list로 형변환
print("lst:" , lst)
chars = set(lst) #lst를 set으로 형변환
print("chars:", chars)
lst = list(chars) #chars를 lst로 형변환

lst.sort()
print("lst:", lst)
print("length of lst:", len(lst))

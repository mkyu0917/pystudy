#문자형
#   시퀸스형
#   변경 불가(immutable) 자료형이에요.
str1 = "Life is too short, you need Python"
str2 = "Welcome Python"
#타입 판별
print(type(str1), type(str2))
#instance 판별
print(str1,"str?:", isinstance(str1, str))

# 여러 줄 문자열
multiline = """
Java
Python
Linux
"""
print(multiline)

#문자열 ",' 사용가능
#print("I said "Yes"")
# Solution 1:
print('I said "Yes"')
# Solution 2: 이스케이프 문자(\)를 활용합니다.
print("I said  \"Yes\"")

#문자열의 인덱싱, 슬라이싱, len 
print(len(str1)) # 길이 :len
print(str1[5])  # 인덱스 접근 가능: 시퀸스형
print(str1[5:7]) # 슬라이싱
print(str1[5:])  # 생략하면 끝까지
print(str1[:6])  # 앞을 생략하면 처음부터
print(str1[:])   # 시퀸스 전체

#str[0] = '1' #변경 안됨 - 변경 불가 객체

# 대소문자관련
# upper() : 전체 대문자
# lower() : 전체 소문자
# swapcase() : 대 <-> 소문자 전환
#capitalize() : 첫 문자 대문자로
# title: 각 단어의 첫글자 대문자로
str3 = str1.lower().title() #메서드 연결 (chaining)

print(str3)

#검색관련
print("count()",str1.count("short")) #검색어의 갯수
print("find()", str1.find("Python")) # 문자열 내 검색
print("find()", str1.find("Life",6)) # 6번 인덱스부터 LIfe를 검색
print("rfind()", str1.rfind("Life")) # 우측으로부터 검색

print("find() 없는 값: ",str1.find("Java"))
#찾는 내용이 없으면 -1을 반환
print("index(): ",str1.index("Python"))
#print("index() 없는 값: "+str1.index("Java")) # 없으면 ValueError

#분리와 결합
print("====분리, 결합====")
s ="Java and Python"
lines ="""\
Java
Python
Linx
Oracle"""

#판별관련
# isdigit() : 형태가 숫자형태인가
# isalpha() : 알파벳 형태인가
# islower() : 소문자 형태인가
# isupper() : 대문자 형태인가
# isspace() : 공백문자 형태인가

num = input("정수를 입력하세요") #문자열을 입력받는다
result = num * 2 #2번 시퀸스 반복
print("result:", result)
'''
#solution 1:
result = int(num) * 2
print("result:", result)
'''
#solution 2:
if num.isdigit():
    result = int(num) * 2
else:
    result = "정수가 아니에요."    
print("result: ",result)

# 분리: split - ' '문자를 기준으로 분리
print(s.split()) #공백 문자 기준 분리
print(s.split("and")); #특정 문자열 기준 분리

# 합치기 : join
t=s.split(" and ")
# : 문자를 넣어  합쳐보겠습니다.
print(":".join(t)) # :값을 기준으로 문자열을 합침
s2 = "abc:def:ghi:jkl"
# : 기준 분리한 후 -> 2개만 가져오기
print(s2.split(":",2))  #왼쪽 :을 기준으로 2개분리
print(s2.rsplit(":",2)) # 오른쪽 :을 기준으로 2개분리

#문자열을 기준으로 
print(lines.splitlines())

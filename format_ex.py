#format_ex.py
#문자열 서식

#서식 문자
'''
%s : 문자열
%d : 정수
%f : 부동소수
%% : %ㄹl터럴

'''

format = "I have %d apples"
print(format % 10)

print("Interest Rate is %.2f%%" %1.24) # %x.yf 정수자리 x까지출력, y소수점자리 

# 두 개 이상의 값을 넣고 싶을때
format = "total: %d개, get: %d개"
print(format % (10,3))

#format과 값의 형식이 일치하지 않으면 TypeError 발생

format_str = "I have{} apples, and i ate {} apples."
print(format_str.format(5, 3))

# 서식에 설정된 공간의 개수와 실제 값의 개수가 적으면 IndexError 발생
print(format_str.format(10, 3, 1))
#print(format_str.format(10)) # Tuple IndexError

#이름 기반의 포맷
format_str = "I have {total} apples, and I ate {num} apples."
print(format_str.format(total = 10, num = 3))
#print(format_str.format(totla = 10)) key Error

#dict 객체를 이용한 포맷
print(format_str.format_map({"total": 10 , "num": 3})) 

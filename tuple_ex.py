#tuple_ex.py
# 튜플
#   시퀸스형, 변경불가 자료형 

# 튜플 생성()
t=(1, 2, 3)
print(t, type(t))

# ()를 생략해도 튜플로 인식
t = 1,2, "Python"
print(t, type(t))

#연결 : +
t2 = t +(3,4,5)
print("t2", t2)

#반복 : *
print(t * 3)

#인덱싱과 슬라이싱 가능
# t2에서 "python,3,4"를 추출해보십
print(t2[2:5])

# 길이를 얻어 오닏
print('len:' , len(t2))

print("-----------------")
print("Packing & unpacking")
# Packing, Unpacking
print('t2 :', t2)

a, b, c, d, e, f = t2 # t2에 있는 값을 변수에 한번에 할당
print("Unpacking:",a,b,c,d,e,f)
'''
#튜플의 요소보다 변수의 수가 더 적을 때
a, b =t2
print(a,b) #ValueError: too many values to unpack 
'''

a, *b = t2 #a에 하나 할당 b에 튜플의 나머지 모든것 할당
print(a, b)

a, b, *c, d, e = t2# C빼고 각각 하나씩 할당, c에 3,4번 같이 할당
print(a, b, c, d, e)

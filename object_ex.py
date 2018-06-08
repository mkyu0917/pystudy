#object_ex.py

print("id 3:",id(5))

#변수에 3을 담는다
# 3 객체를 만들고
# 변수에 3객체의 ID를 연결 심볼 테이블에 저장

a = 3
# a의 id값을 확인해 봅시다.
print("id a:",id(a)) #객체의 주소값을 공유

b = 3
print("id b:", id(b))

b = 4
print("id b:", id(b))

# 객체 심볼 테이블

g_a = 2018
g_b = "symbol"

#글로벌 영역
def f(): #로컬영역변수 확인을 위한 함수
    l_a = "local"
    l_b = 5
    print(locals())#로컬 스코프의 심볼 테이블


print("-------------- : local")
f()
print("-------------- : global")
print(globals()) # 이 영역안에 f를 출력할 수 있는가

print("f" in globals().keys()) #f가 딕션안 key값에 있는가

# 객체 복사
print("------------- object Copy")
x = [1, 2, 3]
y = x
print(x==y)
print(hex(id(x)), hex(id(y)))

x[1] = 4
print(y[1])

# 복제의 시도:1
y = x[:] #슬라이싱을 이용한 복제
print("x", x) #슬라이싱을 이요한 복제로 y에 할당하여 값은 같지만 주소값이 다름
print("y", y)

x[1] = 0
print(y[1])

# 복제의 시도2 : copy 모듈의 활용
import copy

y = copy.copy(x) #
print(x is y) #==로 해도됨 주소값 비교는 is
print("x:", x)
print("y:", y)
x[1] =100
print("x:", x)
print("y:", y)

# 깊은 복제
a = [1, 2, 3]
b = [4, 5, a]
x = [a, b, 100]

print("a:", a)
print("b:", b)
print("x:", x)

y = copy.copy(x)
print("y:", y)

a[1] = 0

print("a:", a)
print("b:", b)
print("x:", x)
print("y:", y)

# deepcopy 객체안의 객체의 값까지 완전히 복제
y = copy.deepcopy(x)
print("a:", a)
print("b:", b)
print("x:", x)
print("y:", y)

a[1] = 100

print("x:", x)
print("y:", y)

# deepcopy는 객체에서 아주 유용하다.
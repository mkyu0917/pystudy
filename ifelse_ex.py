# 조건문 if ~ elif ~ else

n = -2

if n>0:
    print("didtn")
elif n<0:
    print("양수")
else:
    print("0")

    #if는 중첩에서 용할 수 없다
    #조건이 여러개일 경우: and , or등 놀리연산자를 이용해서 조건을 조합할 수 있다.

    #조건 필요식
    # Java, C의 3항연산과 비슷
money = 10000
print("by taxi" if money >= 10000 else "bybus")
    
money = 0
print("by taxi" if money >= 10000 else "on foot" if money == 0 else "by bus")

    #in not in : 포함관계를 나타내는 연산
    #리스트 내보도 같이 해 봅시다.
source = [x for x in range(1,100,2)] #리스트 내포
    
if 2 in source:
    print("2를 포함하고 있습니다.")
else:
    print("2를 포함하고 있지 않습니다.")   
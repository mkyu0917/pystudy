#논리합 (or) : 둘 중 하나가 True 면 True
a=2
b=3

print(a % 2==0 or b % 3 == 0) #a가 2의 배수이거나 b가 3의 배수입니까?
print("------");
#논리곱 (and) : 둘다 T여야 True
print(a > 0 and b< 0)
print("------");
#논리 부정 (not) : 논리값을 반대로 True --> False, False -> True
print(a > 10) # False
print(not a> 10) # 논리부정
print(not(a%2 == 0 and b % 3 ==0)) #일괄 부정
print("");

a=1
print(a.is_integer)
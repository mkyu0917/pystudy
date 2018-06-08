# paint.py
# point를 임포트하여 사용
from point import Point

p1 = Point(10,10)
print("p1", p1)
print("repr",repr(p1))
print("instance count:", Point.instance_count)
p2 = Point(20, 20)
print("instance count:", Point.instance_count)
print("p2", p2)
print("repr",repr(p2))  #repr 메세지를 확인해봅시당.
print("instance count:", Point.instance_count)

p2_copy = eval(repr(p2)) #문자열 복사 할때 repr쓴당
print("p2_copy:", p2_copy)

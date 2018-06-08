#module test
#모듈 임포트

import math
import mymod

#모둘명을 앞에 붙이고 객체를 사용할 수 있게 됩니다.
print(math.pi)
print(mymod.pi)

r = 10
print("Round: ", math.pi * r**2)
print("Round: ", mymod.pi * r**2)

# 어떤 모듈이 현재 로드 되어있는가
import sys
#현재 로드된 모듈의 목록을 출력
#print(sys.modules)
#mymod 모듈은 로드되었는가?
module = sys.modules.keys()

print("YES" if "mymod" in modules else "NO")
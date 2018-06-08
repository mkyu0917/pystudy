#list_ex.py
#리스트 예제

# 리스트의 생성[]
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("l:",l)
print("type l:", type(l))

#인덱스접근
print("l[0]: ", l[0])
#리스트의 길이를 구해봅시다.
print("length: ", len(l))

#연결
print(l+[11, 12, 13]) #확장한게 아니고 그냥 연결만 한것이기 때문에 원래것을 출력해도 변화가 없음
print(l)

# 슬라이스( 슬라이스를 이용해서 부분집합 교체 삭제 가능)
print(l[3:6])

# 슬라이스를 이용한 삭제
l[3:6] = []
print(l)

a = [1, 2, 3]
print("a", a)

if 4 in a: # a 안에 4가 있느냐
    print(a.index(4)) #요소의 인덱스 반환
else:
    print("없어요")

# 항목 추가 : append
a.append(4)
print("a", a)

# 항목 삽입 : insert
a.insert(3, 5)
print("a:", a)

#항목 개수 확인 : count
print("3의 갯수는?",[1, 2, 3, 1, 2, 3].count(3))

#리스트 뒤집기
a.reverse()
print("a:", a)

#항목의 정렬 : sort
a.sort()
print("a:",a)

#항목의 삭제 : remove
a.remove(5)
print("a:",a)

# 리스트의 확장: extend
a.extend([5, 6, 7,])
print("a:", a)
print("똠양꿈")
print("빵구똥구")

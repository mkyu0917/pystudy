lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

slice = lst[3:7] #인덱스의 유의주의
print("slice:" ,slice)
slice.reverse() # 순서 뒤집기
lst[3:7] = slice
print("lst:", lst)




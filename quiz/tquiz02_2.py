lst = [1, 3.14, 'python', 7, 89.1, 3]

lst_cleaned = []

for item in lst:
    #if isinstance(item, int) or isinstance(item, float):
    if isinstance(item, (int, float)): # 아이템이 int이거나 float 이거나
        lst_cleaned.append(item)

print(lst_cleaned)

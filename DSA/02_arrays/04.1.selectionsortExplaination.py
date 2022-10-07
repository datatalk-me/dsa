
tmp = []

lst = []

j = 0

array = [50,25,38,44,99,16,11,21]

for i in array:
    if i > j:
        tmp.append(i)
        for i in array:
            if tmp[0] > i:
                lst.append(i)

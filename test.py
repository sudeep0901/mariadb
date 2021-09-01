import numpy as np

arr_zeros= np.zeros((35,35))


for i in arr_zeros:
    index = 0
    k = 0
    print(i)
    for j in i:
        if k > 6:
            k = 0
        else:
            k = k + 1
            print(k)
        i[index] = k
        index = index + 1
        # print(index)
    print(i)
print(arr_zeros)

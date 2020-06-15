import random


def insert_sort(array):
    N = len(array)
    for i in range(N):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    return array


array = [random.randint(0, 100) for _ in range(100)]
print(insert_sort(array))


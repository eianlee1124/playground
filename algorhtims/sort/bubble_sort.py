import random


def bubble_sort(array):
    N = len(array)
    for i in range(N):
        is_sorted = True
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
                is_sorted = False
        if is_sorted:
            break
    return array


if __name__ == "__main__":
    array = [random.randint(0, 1000) for _ in range(1000)]
    print(bubble_sort(array))
            

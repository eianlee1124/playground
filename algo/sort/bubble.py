def bubble_sort(array):
    N = len(array)
    for i in range(N):
        for j in range(N-i-1):
            is_sorted = True
            if array[i] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                is_sorted = False
        if is_sorted:
            break
    return array

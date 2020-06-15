"""
`is_sorted` boolean 플래그는 꼭 필요하진 않지만
불필요한 순회를 하지않게끔 최적화 함
"""

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

            

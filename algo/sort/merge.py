#!/usr/bin/env python3



from random import randint
from timer import timer

def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0
    
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
            
        if index_right == len(right):
            result += left[index_left:]
            break
        
        if index_left == len(left):
            result += right[index_right:]
            break

    return result

    
def merge_sort(array):
    if len(array) < 2:
        return array
    
    midpoint = len(array) // 2
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:])
    )
    
    
if __name__ == "__main__":
    ARRAY_LENGTH = 10000
    array = [randint(0, 1000) for _ in range(ARRAY_LENGTH)]
    timer(algorithm='merge_sort', array=array)
    timer(algorithm='sorted', array=array)
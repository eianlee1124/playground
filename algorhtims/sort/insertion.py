#!/usr/bin/env python3


from random import randint
from timer import timer


def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item





if __name__ == "__main__":
    
    ARRAY_LENGTH = 1000
    array = [randint(0, 1000) for _ in range(ARRAY_LENGTH)]
    # timer(algorithm='insertion_sort', array=array)
    timer(algorithm='sorted', array=array)
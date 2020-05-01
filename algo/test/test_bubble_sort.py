import os
import sys
import time
import timeit
from random import randint
sys.path.append(os.path.abspath(os.getcwd()))


if __name__ == "__main__":    
    from sort.bubble import bubble_sort
    from util.timer import timer

    ARRAY_LENGTH = 10000
    array = [randint(0, 1000) for _ in range(ARRAY_LENGTH)]
    
    timer(algorithm='bubble_sort', array=array)



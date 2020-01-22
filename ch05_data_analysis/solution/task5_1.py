"""
    task5_1.py solution - There are four parts to this exercise, each is described
                          individually below.
"""
import numpy as np


# --------------------------------------------------------------------------
#  Part 1 -  Create an n x n array, with each row counting from 1 up to n
#            This version uses tile()
#
def create_array1(n):
    return np.tile(np.arange(1, n+1), [n, 1])


print('An array of n x n size with increasing row values:')
print(create_array1(5))


# --------------------------------------------------------------------------
#  Part 1 (alternate way) -  Repeated, this time without using tile()
#
def create_array1b(n):
    return np.array([np.arange(1, n+1),]*n)


print('Without using tile...')
print(create_array1b(5))


# --------------------------------------------------------------------------
#  Part 2 -  Providing a start/stop value
#
def create_array2(start, stop):
    width = stop - start + 1
    return np.tile(np.arange(start, stop + 1), [width, 1])

print('Using a start/stop value...')
print(create_array2(8, 11))


# --------------------------------------------------------------------------
#  Part 3 -  Returning only "middle values"
#
def create_array3(start, stop):
    width = stop - start + 1
    arr = np.tile(np.arange(start, stop + 1), [width, 1])
    return arr[1:width-1, 1:width-1]


print('Returning only middle values...')
print(create_array3(8, 11))


# --------------------------------------------------------------------------
#  Part 4 -  Second array filled with a value, but sized to the array returned from part 3.
#
def create_second_array(arr, fill_val):
    return np.full(arr.shape, fill_val)


print('A second array containing a fill value...')
arr = create_array3(8, 11)
print(create_second_array(arr, 25))

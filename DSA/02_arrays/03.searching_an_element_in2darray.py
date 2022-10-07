import numpy as np


# Create a 2D array
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# # Search for the element 7 using brute force method or approach
# # here the time complexity is O(n^2)
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j] == 2:
#             print("Element found at index", i, j)
#             break



# another way to search for an element in a 2D array
# using numpy.where() method


def Search2dSortedArray(array, target):
    # Search for the element x in the 2D array
    i = 0

    j = len(array[0]) - 1       # last column index (no of columns) 4 - 3  -2 1

    n = len(array)              # number of rows


    # time complexity for this O(n)
    while i < n and j >= 0:
        if array[i][j] == target:
            return i, j, array[i][j]
        elif array[i][j] > target:
            j -= 1
        else:
            i += 1
    return -1


# 2D array
array = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
result  = Search2dSortedArray(array, target)
print('The result is: ', result)
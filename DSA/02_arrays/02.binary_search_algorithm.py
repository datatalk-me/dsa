# binary search algorithm

# BinarySearch Algorithm implementation in Python using iteration



# complexity O(log n)

def binarysearch(arr,search_element,n):
    start = 0
    end = n-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == search_element:
            return mid
        elif arr[mid] < search_element:
            start = mid+1
        else:
            end = mid-1
    # If element is not found
    return -1

arr = [1,2,3,4,5,6,7,8,9,10]

search_element = 9
n = len(arr)
result = binarysearch(arr,search_element,n)
print('Element found at index: ',result)



# BinarySearch Algorithm implementation in Python using recursion
# recursion is calling a function inside a function


# second approach


def BinarySearch(array, i, j, search):
    # singele element in a array
    if i == j:
        # for single element the time complexity is O(1) which is constant
        if array[i] == search:
            return i
        else:
            return -1
    # more than one element in array
    else:
        mid = (i+j)//2                     # we can also use (i + (j-i)//2)
        if array[mid] == search:
            return mid
        elif array[mid] > search:
            return BinarySearch(array, i, mid-1, search)
        else:
            return BinarySearch(array, mid+1, j, search)
    


array = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
i = 0
j = len(array) - 1
search = 80
result = BinarySearch(array, i, j, search)
print('Element found at index: ',result)








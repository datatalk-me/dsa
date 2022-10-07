
# over all time complexity is O(n) for linear search

# LinearSearch Algorithm implementation in Python

def linearsearch(arr,search_element,n):
    for i in range(n):
        if arr[i] == search_element:
            return i
    # If element is not found
    return -1

arr = [1,2,3,4,5,6,7,8,9,10]

search_element = 5
n = len(arr)
result = linearsearch(arr,search_element,n)
print('Element found at index: ',result)
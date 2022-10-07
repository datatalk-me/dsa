# Bubble sort implementation


def BubbleSort(arr):
    # sort the array using bubble sort algorithm
    # time complexity is O(n^2)
    # space complexity is O(1)
    # for each pass the maximum element is moved to the end
    for i in range(len(arr) - 1):
        print('i value is: ',i)
        for j in range(len(arr)-i-1):
            print('len(arr)-i-1 value is: ',len(arr)-i-1)
            print('j value is: ',j)
            if arr[j] > arr[j+1]:
                print('arr[j] is {} and arr[j+1] is {}: '.format(arr[j],arr[j+1]))
                print('Swapping', arr[j], 'and', arr[j+1])
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print('arr is: ',arr)

    return arr

array = [50,25,38,44,99,16,11,21] 
result = BubbleSort(array)
print('The result is: ', result)
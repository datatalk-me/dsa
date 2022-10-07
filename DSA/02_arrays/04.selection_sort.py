
# selection sort algorithm

def SelectionSort(arr):
    # sort the array using selection sort algorithm
    # time complexity is O(n^2)
    # space complexity is O(1)
    # for each pass only one swap is done
    for i in range(len(arr)): #25
        print('i value is: ',i)
        # minimum index takes the index of the minimum element in the array at each iteration
        min_index = i
        print('min_index value in i iteration: ',min_index)
        for j in range(i+1, len(arr)):
            print('j value is: ',j)
            if arr[min_index] > arr[j]:
                print('arr[min_index] is {} and arr[j] is {}: '.format(arr[min_index],arr[j]))
                min_index = j
                print('min_index value in j iteration: ',min_index)
        # swap the minimum element with the element at the current index
        print('Swapping', arr[i], 'and', arr[min_index])
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print('arr is: ',arr)

    return arr

array = [50,25,38,44,99,16,11,21]
result = SelectionSort(array)
print('The result is: ', result)

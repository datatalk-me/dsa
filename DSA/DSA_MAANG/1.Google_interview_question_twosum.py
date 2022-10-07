# given an array of integers return indices of the two numbers such that they add up to a specific target

# example 1:
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# but this is a brute force solution, it is not the best solution
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))


# this is the best solution
def twoSum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], i]
        d[num] = i
    return d

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
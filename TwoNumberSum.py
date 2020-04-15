#Two Number Sum

"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
If any two numbers in the input array sum up to the target sum, the function should return them in an array, in
any order. If no two numbers sum up to the target sum, the function should return an empty array.

You can assume there will be at most one pair of numbers summing up to the target sum.
"""

def twoNumberSum(array, targetSum):
    for i in range(0, len(array)-1):
        for j in range(i+1, len(array)):
            currentSum = array[i] + array[j]
            if currentSum == targetSum:
                return sorted([array[i],array[j]])
    return []


#alternate solution
def twoNumberSum(array,targetSum):
    array.sort()
    left = 0 
    right = len(array) - 1 
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return sorted([array[left], array[right]])
        if currentSum < targetSum:
            left += 1
        if currentSum > targetSum:
            right -= 1
    return []


print(twoNumberSum([ 3, 5, -4, 8, 11, 1, -1, 6], 10))
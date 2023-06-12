'''
Link: https://leetcode.com/problems/two-sum/description/
Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add 
up to target. You may assume that each input would have exactly one solution, and you may not use the same 
element twice. You can return the answer in any order.
'''
# O(n) solution
def twoSum(nums, target):
    prevMap = {}
    for i, el in enumerate(nums):
        difference = target - el
        if difference in prevMap:
            return [prevMap[difference], i]
        prevMap[el] = i
        
# O(n^2) solution
def twoSum2(nums, target):
        result = []
        for i in range(len(nums)):
            for j in range(i+ 1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
        return result

# should return [0, 1]
twoSum([2,7,11,15], 9)
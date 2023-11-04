'''
Link: https://leetcode.com/problems/two-sum/description/
Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add 
up to target. You may assume that each input would have exactly one solution, and you may not use the same 
element twice. You can return the answer in any order.
'''
# # O(n) solution
# def twoSum(nums, target):
#     prevMap = {}
#     for i, el in enumerate(nums):
#         difference = target - el
#         if difference in prevMap:
#             return [prevMap[difference], i]
#         prevMap[el] = i

def two_sum(nums, target):
    pos_map = {}
    for i, el in enumerate(nums):
        diff = target - el
        if diff in pos_map:
             return [pos_map[diff], i]
        pos_map[el] = i

# O(n^2) solution
def two_sum2(nums, target):
        for i in range(len(nums)):
            for j in range(i+ 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# should return [0, 1]
assert two_sum([2,7,11,15], 9) == [0, 1]
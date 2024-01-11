'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

def two_sum(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i

# Example 1:
nums1 = [2, 7, 11, 15]
target1 = 9
result1 = two_sum(nums1, target1)
print(result1)  # Output: [0, 1]

# Example 2:
nums2 = [3, 2, 4]
target2 = 6
result2 = two_sum(nums2, target2)
print(result2)  # Output: [1, 2]

# Example 3:
nums3 = [3, 3]
target3 = 6
result3 = two_sum(nums3, target3)
print(result3)  # Output: [0, 1]



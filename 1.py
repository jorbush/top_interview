"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

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

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2)
time complexity?
"""


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    return two_sum(nums, target)


def two_sum(nums, target, k=0):
    if len(nums) == 0:
        return None
    current = nums[k]
    ind = sum_target(nums, target, current, k + 1)
    if ind is not None:
        return [k, ind]
    return two_sum(nums, target, k + 1)


def sum_target(nums, target, first_num, k):
    if k >= len(nums):
        return None
    current = nums[k]
    if first_num + current == target:
        # print(f'{first_num} {current} {k}')
        return k
    return sum_target(nums, target, first_num, k + 1)


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    print(twoSum(nums, target))

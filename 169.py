"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109


Follow-up: Could you solve the problem in linear time and in O(1) space?
"""


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return majority_element(nums, dict())


def majority_element(nums, dictionary):
    """
    :type nums: List[int]
    :type dictionary: dict
    :rtype: int
    """
    if len(nums) == 0:
        return max(dictionary, key=dictionary.get)
    current = nums.pop(0)
    if dictionary.get(current) is None: dictionary[current] = 1
    else: dictionary[current] += 1
    return majority_element(nums, dictionary)


if __name__ == "__main__":
    nums = [3, 2, 3]
    print(majorityElement(nums))

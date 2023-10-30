"""
Given an integer array nums, rotate the array to the right by k steps,
where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105


Follow up:

Try to come up with as many solutions as you can.
There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""


def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    return rotate_list(nums, k, ['_' for x in range(len(nums))], 0, set())
    # return rotate_slicing(nums, k)
    # return best_rotate(nums, k)


def best_rotate(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]


def rotate_slicing(nums, k):
    if k < len(nums):
        nums[:] = nums[-k:] + nums[:-k]
    else:
        for j in range(k):
            nums[:] = nums[-1:] + nums[:-1]


def rotate_list(nums, k, new_nums, ind, seen_ind):
    if ind == len(nums):
        nums.clear()
        nums.extend(new_nums)
        return None
    current = nums[ind]
    if ind not in seen_ind:
        seen_ind.add(ind)
        move_position(new_nums, k, ind, current)
    new_ind = ind + 1
    return rotate_list(nums, k, new_nums, new_ind, seen_ind)


def move_position(nums, k, pos, value):
    new_position = pos + k
    length = len(nums)
    if new_position >= length:
        new_position %= length
    nums[new_position] = value


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate(nums, k)
    print(nums, k)

"""
You are given an integer array nums. You are initially positioned at
the array's first index, and each element in the array represents your
maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
jump length is 0, which makes it impossible to reach the last index.

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""


def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return can_jump_rec(nums, 0, 0)


def can_jump_rec(nums, ind, max_ind_reachable):
    if ind == len(nums) - 1:
        return max_ind_reachable >= len(nums) - 1
    if ind > max_ind_reachable:  # Can't move past the current index
        return False
    max_ind_reachable = max(max_ind_reachable, nums[ind] + ind)
    # print(f'max={max_ind_reachable} num={nums[ind]} ind={ind}')
    return can_jump_rec(nums, ind + 1, max_ind_reachable)


def can_jump(nums, ind, register, max_ind_reachable):
    if len(nums) == 1:
        return True
    if ind == len(nums) - 1:
        return False
    print(register, max_ind_reachable)
    if nums[ind] not in register:
        if ind <= max_ind_reachable:
            result, max_ind_reachable = can_achieve_finish(nums, ind, register, max_ind_reachable)
            if result:
                return True
        else:
            return False
    return can_jump(nums, ind + 1, register, max_ind_reachable)


def can_achieve_finish(nums, ind, register, max_ind_reachable):
    if ind >= len(nums) - 1:
        # print(f'win -> {nums} {ind}')
        return True, max_ind_reachable
    jump = ind + nums[ind]
    print(f'jump -> {nums} {ind} {jump}')
    if jump not in register:
        register.add(jump)
        max_ind_reachable = max(max_ind_reachable, jump)
        return can_achieve_finish(nums, jump, register, max_ind_reachable)
    return False, max_ind_reachable


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    nums_2 = [3, 2, 1, 0, 4]
    nums_e = [1, 1, 2, 2, 0, 1, 1]
    print(canJump(nums))

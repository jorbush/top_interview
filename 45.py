"""
You are given a 0-indexed array of integers nums of length n. You are
initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump
from index i. In other words, if you are at nums[i], you can jump to
any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases
are generated such that you can reach nums[n - 1].

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""


def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return jump_bfs(nums, 0, 0, 0, 0)


def jump_bfs(nums, ind, min_jumps, max_ind_reachable, end):
    if ind == len(nums) - 1:
        return min_jumps
    max_ind_reachable = max(max_ind_reachable, ind + nums[ind])
    if max_ind_reachable >= len(nums) - 1:  # Have already achieved the last element
        min_jumps += 1
        return min_jumps
    if ind == end:                  # Visited all the items on the current level
        min_jumps += 1              # Increment the level
        end = max_ind_reachable     # Make the queue size for the next level
    return jump_bfs(nums, ind + 1, min_jumps, max_ind_reachable, end)


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print(jump(nums))

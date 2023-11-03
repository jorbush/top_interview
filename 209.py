"""
Given an array of positive integers nums and a positive integer target,
return the minimal length of a
subarray
 whose sum is greater than or equal to target. If there is no such subarray,
 return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem
constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another
solution of which the time complexity is O(n log(n)).

"""


def minSubArrayLen(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    # return min_sub_array_len(target, nums, 1)
    return min_sub_array_len_sw(target, nums)


def min_sub_array_len_sw(target, nums):
    left_ind, current_sum, min_length = 0, 0, float('inf')

    for right_ind in range(len(nums)):
        current_sum += nums[right_ind]
        # print(f'move right -> {nums[left_ind:right_ind]} {current_sum}')
        while current_sum >= target:
            # print(f'solution found')
            new_length = right_ind - left_ind + 1
            min_length = min(min_length, new_length)
            # print(f'    move left -> {nums[left_ind:right_ind+1]} = {current_sum}, m_l = {min_length}')
            current_sum -= nums[left_ind]
            left_ind += 1

    return min_length if min_length != float('inf') else 0


def min_sub_array_len(target, nums, window_size):
    if window_size > len(nums):
        return 0
    min_len_current_ws = sliding_window(nums, window_size, target, 0)
    if min_len_current_ws != 0:
        return min_len_current_ws
    return min_sub_array_len(target, nums, window_size + 1)


def sliding_window(elements, window_size, target, ind):
    if len(elements) - window_size + 1 <= ind:
        return 0
    sum_elements = elements[ind:ind + window_size]
    current_sum = sum(sum_elements)
    # print(f'solution -> {window_size} with {sum_elements} = {current_sum}')
    if current_sum >= target:
        # print(f'best solution -> {window_size} with {sum_elements} = {current_sum}')
        return window_size
    return sliding_window(elements, window_size, target, ind + 1)


if __name__ == "__main__":
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(minSubArrayLen(target, nums))

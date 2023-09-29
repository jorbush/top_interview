"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To
accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1 Output: [1] Explanation: The arrays we are merging are [] and [1]. The
result of the merge is [1]. Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure
the merge result can fit in nums1.


Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109


Follow up: Can you come up with an algorithm that runs in O(m + n) time?

"""


def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    insert_numbers(nums1, m, nums2[0:n], n)


def insert_numbers(nums1, m, nums2, n):
    # print(f"nums1:{nums1} m:{m} nums2:{nums2} n:{n}")
    if n == 0:
        del nums1[m:]
        return None
    n2 = nums2.pop(0)
    ind = get_index(n2, nums1[0:m])
    nums1.insert(ind, n2)
    return insert_numbers(nums1, m + 1, nums2, n - 1)


def get_index(num, nums, i=0):
    if len(nums) == 0:
        return i
    current = nums.pop(0)
    # print(num, current, num < current, nums, i)
    if num < current:
        return i
    return get_index(num, nums, i + 1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    merge(nums1, 3, [2, 5, 6], 3)
    print(nums1) # len of m

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

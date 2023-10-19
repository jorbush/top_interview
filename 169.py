"""

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

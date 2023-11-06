"""
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the
letters of a different word or phrase, typically using all the
original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from collections import defaultdict


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # return group_anagrams(strs, 0, dict())
    return group_anagrams_opt(strs, 0, defaultdict(list))


def group_anagrams_opt(strs, ind, anagrams):
    if ind == len(strs):
        return list(anagrams.values())
    word = strs[ind]
    register_count_letters(word, anagrams)
    return group_anagrams_opt(strs, ind + 1, anagrams)


def register_count_letters(word, register):
    count = [0] * 26  # represents the frequency of each letter
    for char in word:
        count[ord(char) - ord('a')] += 1
        # ord('a') = 97, ord('b') = 98, ...
    register[tuple(count)].append(word)


def group_anagrams(strs, ind, anagrams):
    if ind >= len(strs):
        return list(anagrams.values())
    current = strs[ind]
    existing_anagram = has_anagram(anagrams, current)
    if existing_anagram is not None:
        anagrams[existing_anagram] += [current]
    else:
        anagrams[current] = [current]
    return group_anagrams(strs, ind + 1, anagrams)


def has_anagram(anagrams, current):
    for x in anagrams.keys():
        if current == x or is_anagram(x, current, dict(), dict(), 0):
            return x


def is_anagram(x, y, dict_x, dict_y, ind):
    if len(x) != len(y):
        return False
    if ind == len(x):
        return dict_x == dict_y
    key_x = x[ind]
    if key_x in dict_x:
        dict_x[key_x] += 1
    else:
        dict_x[key_x] = 1
    key_y = y[ind]
    if key_y in dict_y:
        dict_y[key_y] += 1
    else:
        dict_y[key_y] = 1
    return is_anagram(x, y, dict_x, dict_y, ind + 1)


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    str_f = ["", ""]
    print(groupAnagrams(strs))

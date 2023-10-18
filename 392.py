"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
"""


def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    return is_subsequence(list(s), list(t))


def is_subsequence(s, t):
    """
    :type s: list
    :type t: list
    :rtype: bool
    """
    if len(s) == 0:
        return True
    current = s.pop(0)
    if is_in_sequence(current, t):
        return is_subsequence(s, t)
    return False


def is_in_sequence(c, t):
    if len(t) == 0:
        return False
    current_t = t.pop(0)
    if c == current_t:
        return True
    return is_in_sequence(c, t)


if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    print(isSubsequence(s, t))

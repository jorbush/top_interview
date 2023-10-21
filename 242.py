"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    return is_anagram(list(s), list(t))


def is_anagram(s, t):
    if len(s) == 0:
        return len(t) == 0
    if not has_letter(s.pop(0), t):
        return False
    return is_anagram(s, t)


def has_letter(c, t, k=0):
    if k == len(t):
        return False
    if c == t[k]:
        t.pop(k)
        return True
    return has_letter(c, t, k + 1)


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))

"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true


Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""


def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    return is_isomorphic(list(s), list(t), dict(), set())


def is_isomorphic(s, t, dictionary, register):
    if len(s) == 0:
        return len(s) == len(t)
    current_s, current_t = s.pop(0), t.pop(0)
    if dictionary.get(current_s) is None:
        if current_t not in register:
            dictionary[current_s] = current_t
            register.add(current_t)
        else: return False
    else:
        if dictionary[current_s] is not current_t: return False
    # print(dictionary, register)
    return is_isomorphic(s, t, dictionary, register)


if __name__ == "__main__":
    s = "paper"
    t = "title"
    print(isIsomorphic(s, t))

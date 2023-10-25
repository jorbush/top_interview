"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    parenthesis = {
        "]": "[",
        ")": "(",
        "}": "{"
    }
    return is_valid(list(s), [], parenthesis)


def is_valid(s, acc, parenthesis):
    if len(s) == 0:
        return len(acc) == 0
    current = s.pop(0)
    if is_open_parentheses(current):
        acc.insert(0, current)
    else:
        if len(acc) == 0 or parenthesis[current] != acc.pop(0):
            return False
    return is_valid(s, acc, parenthesis)


def is_open_parentheses(c):
    return c == "(" or c == "[" or c == "{"


if __name__ == "__main__":
    s = "([)]"
    print(isValid(s))

"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and
numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    alphanumeric = ''.join(filter(str.isalnum, s)).lower()
    return alphanumeric == alphanumeric[::-1]
    # return recursive_palindrome(list(s.lower()))


def recursive_palindrome(s, palindrome="", palindrome_reversed=""):
    if len(s) == 0:
        return palindrome == palindrome_reversed
    current = s.pop(0)
    if current.isalnum():
        palindrome += current
        palindrome_reversed = current + palindrome_reversed
    # print(f'current={current} alpha={current.isalpha()} palindrome={palindrome} p_r={palindrome_reversed}')
    return recursive_palindrome(s, palindrome, palindrome_reversed)


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    k = isPalindrome(s)
    print(f'k={k}')

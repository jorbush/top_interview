"""
Given a string s consisting of words and spaces, return
the length of the last word in the string.

A word is a maximal
substring
 consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

"""


def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    return length_of_last_word(s)


def length_of_last_word(s, last_char=" ", length_lw=0, ind=0):
    """
    :type s: str
    :rtype: int
    """
    if ind == len(s):
        return length_lw
    current = s[ind]
    # print(f'{current} {current != " "} {last_char == " "} {length_lw}')
    if current != " " and last_char == " ":
        new_length = 1
    elif current != " " and last_char != " ":
        new_length = length_lw + 1
    else:
        new_length = length_lw
    return length_of_last_word(s, current, new_length, ind + 1)


if __name__ == "__main__":
    s = "   fly me   to   the moon  "
    print(lengthOfLastWord(s))

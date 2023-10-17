"""
Given two strings ransomNote and magazine,
return true if ransomNote can be constructed by using the letters from
magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""


def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    return construct_ransom_note(list(ransomNote), list(magazine))


def construct_ransom_note(ransom_note, magazine):
    if len(ransom_note) == 0:
        return True
    current = ransom_note.pop(0)
    if char_in_magazine(current, magazine.copy(), magazine):
        return construct_ransom_note(ransom_note, magazine)
    else:
        return False


def char_in_magazine(character, current_magazine, magazine, k=0):
    if len(current_magazine) == 0:
        return False
    current = current_magazine.pop(0)
    if character == current:
        magazine.pop(k)
        return True
    return char_in_magazine(character, current_magazine, magazine, k=k + 1)


if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "aab"
    k = canConstruct(ransomNote, magazine)
    print(f'k={k}')

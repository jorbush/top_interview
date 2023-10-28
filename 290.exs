"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between
a letter in pattern and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false


Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""

defmodule Solution290 do
  #@spec word_pattern(pattern :: String.t, s :: String.t) :: boolean
  def word_pattern(pattern, s) do
    word_pattern_list(String.codepoints(pattern), String.split(s), %{})
  end

  def word_pattern_list([], [], _acc), do: true
  def word_pattern_list([], _s, _acc), do: false
  def word_pattern_list(_pattern, [], _acc), do: false
  def word_pattern_list([ pattern | tail_pattern], [s | tail_s], acc) do
    # IO.inspect acc
    if acc[pattern] do
      if acc[pattern] == s do
        word_pattern_list(tail_pattern, tail_s, acc)
      else
        false
      end
    else
      value = Enum.find_value(acc, fn {_, v} -> v == s end)
      if value do
        false
      else
        word_pattern_list(tail_pattern, tail_s, Map.put(acc, pattern, s))
      end
    end
  end

end

IO.puts Solution290.word_pattern("abba", "dog cat cat dog")  # true
IO.puts Solution290.word_pattern("abba", "dog cat cat fish") # false
IO.puts Solution290.word_pattern("aaaa", "dog cat cat dog")  # false
IO.puts Solution290.word_pattern("abba", "dog dog dog dog")  # false

"""
3. Longest Substring Without Repeating Characters
Medium

14587

747

Add to List

Share
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


def logest_substring(string):
	max_length = 0
	left = 0
	right = 0
	hash_map = {}
	while left < len(string) and right < len(string):
		element = string[right]
		if element in hash_map:
			left = max(left, hash_map[element] + 1)
		hash_map[element] = right
		max_length = max(max_length, (right - left) + 1)
		right += 1
	return max_length

if __name__ == "__main__":
	string1 = "abaabababababa"
	string2 = "abcdefgahfhdjhqwertyuiopasdfghjkl"
	string3 = "a"
	print (f"Max sub-string length of {string1}: {logest_substring(string1)}")
	print (f"Max sub-string length of {string2}: {logest_substring(string2)}")
	print (f"Max sub-string length of {string3}: {logest_substring(string3)}")

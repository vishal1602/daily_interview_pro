# Given a string, find the length of the longest substring without repeating characters.

class Solution:
	def lengthOfLongestSubstring(self, s):
		sub_strs = []
		temp_str = ""
		if not s:
			return 0
		for char in s:
			if char in temp_str:
				sub_strs.append(temp_str)
				temp_str = ""
			else:
				temp_str += char
		if not temp_str:
			sub_strs.append(temp_str)
		return len(max(sub_strs, key=len))

print (Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
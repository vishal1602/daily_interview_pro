# A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find the longest palindromic substring in s.

class Solution: 
    def longestPalindrome(self, s):
      # Fill this in.
        pd = ""
        if s == s[::-1]:
        	return s
        for i in range(0, len(s)):
        	for j in range(i, len(s)+1):
        		substr = s[i:j] 
        		if (substr == substr[::-1]) & (len(substr) > len(pd)):
        			pd = substr
        return pd
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
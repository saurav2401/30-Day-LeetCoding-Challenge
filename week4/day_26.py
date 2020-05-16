'''
Problem Statement:
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 
Constraints:
1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
'''

# Solution:

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # find the length of the strings 
        m = len(text1) 
        n = len(text2) 
        
        def lcs(text1, text2, m, n): 

            if m == 0 or n == 0: 
                return 0
            elif text1[m-1] == text2[n-1]: 
                return 1 + lcs(text1, text2, m-1, n-1)
            else: 
                return max(lcs(text1, text2, m, n-1), lcs(text1, text2, m-1, n))
        return lcs(text1,text2,m,n)

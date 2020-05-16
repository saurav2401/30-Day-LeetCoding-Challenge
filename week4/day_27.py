'''
Problem Statement:
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''

# Solution:

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        if matrix == []:
            return 0
    
        len_r, len_c = len(matrix), len(matrix[0])
        
        if len_r == 0 or len_c == 0:
            return 0
        
        dp = [[0 for i in range(len_c + 1)] for j in range(len_r + 1)]
        max_dim = 0
        
        # Filling up the dp table
        for i in range(len_r):
            for j in range(len_c):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j],dp[i][j+1]) + 1
                    # Finding the max dimension of the square so far
                    max_dim = max(max_dim, dp[i+1][j+1])
                else:
                    dp[i+1][j+1] = 0
        
        return max_dim*max_dim

'''
Problem Statement:
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
'''
# Solution:

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        partial_sum = 0
        
		# table is a dictionary
		# key : partial sum value
		# value : the left-most index who has the partial sum value
		
        table = { 0: -1}
        
        max_length = 0
        
        for idx, number in enumerate( nums ):
            
            # add 1 for 1
            # minus 1 for 0
            
            if number:
                partial_sum += 1
            else:
                partial_sum -= 1
                
            
            if partial_sum in table:
                
                # we have a subarray with equal number of 0 and 1
                # update max length
                
                max_length = max( max_length, ( idx - table[partial_sum] ) )
                
            else:
                # update the left-most index for specified partial sum value
                table[ partial_sum ] = idx
                
        return max_length
            

'''
Problem Statement:
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

# Solution:

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        temp = final =0
        while(final<len(nums)):
            
            if nums[temp] == 0 and nums[final] != 0:
                nums[temp],nums[final] = nums[final],nums[temp]
                
            if nums[temp] != 0:
                temp += 1
            final += 1
        

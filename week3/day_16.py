'''
Problem Statement:
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
'''

# Solution:

class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        
        # Maintaining two stacks
        # 1) left parenthesis's indexes
        # 2) star's ("*") indexes
        left = list()
        star = list()
        
        for i, c in enumerate(s):
            if c == "*":
                star.append(i)
            elif c == "(":
                left.append(i)
            elif c == ")":
                # When encounter "*"
                # Prefer balance out using the left "(" than "*"
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        if len(left) > len(star):
            # Checking the counts of residual left and star
            return False
        
        while left and star:
            # Compare the indexes of left and star
            # Make sure star came aftewards, if not, return False
            if left.pop() > star.pop():
                return False
        
        return True

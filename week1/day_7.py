'''
Problem Statement:
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

# Soltuion:

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        arr = []
        for i in strs:
            key = ''.join(sorted(i))
            if key in temp.keys():
                temp[key].append(i)
            else:
                temp[key]=[]
                temp[key].append(i)
        for i in temp:
            arr.append(temp[i])
        return arr

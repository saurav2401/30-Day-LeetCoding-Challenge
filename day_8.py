class Solution:
    def countElements(self, arr: List[int]) -> int:
        data = []
        count = 0
        n = len(arr)
        for i in range(n+1):
            data.append(0)
        for i in range(n):
            data[arr[i]] += 1
        for i in range(n):
            if data[i] != 0 and data[i+1] != 0:
                count += data[i]
        return count
            
            

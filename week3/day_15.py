class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        final = 0
        n = len(shift)
        for i in range(n):
            if shift[i][0] == 0:
                final -= shift[i][1]
            if shift[i][0] == 1:
                final += shift[i][1]
        final %= n
            
        if final == 0:
            return s
        return s[-final:] + s[:-final]

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
        l = 0

        for r in range(n-1, m):
            substr = s2[l:r + 1]
            if Counter(s1) == Counter(substr):
                return True
            else:
                l += 1
        
        return False
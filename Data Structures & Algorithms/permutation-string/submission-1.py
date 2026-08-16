from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
        
        reference = Counter(s1)
        window = Counter(s2[:n])

        if reference == window:
            return True
        
        for r in range(n, m):
            window[s2[r]] += 1
            window[s2[r - n]] -= 1

            if reference == window:
                return True
        
        return False
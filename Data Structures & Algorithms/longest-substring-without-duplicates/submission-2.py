class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        subs = []

        for char in s:
            if char not in subs:
                subs.append(char)
            else:
                ans = max(ans, len(subs))
                if char == subs[0]:
                    del subs[0]
                else:
                    subs = []
                subs.append(char)
        
        return max(ans, len(subs))
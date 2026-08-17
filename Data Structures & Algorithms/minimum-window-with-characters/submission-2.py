class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)

        if m > n:
            return ""
        
        res, resLen = [-1, -1], float("inf")
        window, dic_t = {}, {}

        for c in t:
            dic_t[c] = 1 + dic_t.get(c, 0)

        l = 0
        have, need = 0, len(dic_t)
        for r in range(n):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in dic_t and window[c] == dic_t[c]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in dic_t and window[s[l]] < dic_t[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res
        return s[l: r + 1] if l != -1 else ''
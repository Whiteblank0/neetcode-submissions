class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        candidates.sort()
        n = len(candidates)

        def dfs(i, t):
            if t < 0:
                return
            
            if t == 0:
                ans.append(path.copy())
                return
            
            for j in range(i, n):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                num = candidates[j]
                path.append(num)
                dfs(j + 1, t - num)
                path.pop()

        dfs(0, target)
        return ans    
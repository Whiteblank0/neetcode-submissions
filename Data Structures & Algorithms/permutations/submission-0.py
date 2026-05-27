class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        path = [0] * n
        on_path = [False] * n

        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            
            for j in range(n):
                if not on_path[j]:
                    path[i] = nums[j]
                    on_path[j] = True
                    dfs(i+1)
                    on_path[j] = False
        
        dfs(0)
        return ans
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)

        def dfs(i, t):
            if t < 0:
                return
            
            if t == 0:
                ans.append(path.copy())
                return
            
            for j in range(i, n):
                num = nums[j]
                path.append(num)
                dfs(j, t - num) 
                path.pop()
        
        dfs(0, target)
        return ans
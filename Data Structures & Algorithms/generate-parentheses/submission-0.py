class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m = 2 * n
        ans = []
        path = [""] * m 

        def dfs(i, ope):
            if i == m:
                ans.append("".join(path))
                return
            if ope < n:
                path[i] = '('
                dfs(i + 1, ope + 1)
            if i - ope < ope:
                path[i] = ')'
                dfs(i + 1, ope)

        dfs(0, 0)
        return ans
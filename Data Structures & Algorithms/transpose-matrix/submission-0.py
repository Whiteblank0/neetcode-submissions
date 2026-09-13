class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix), len(matrix[0])
        res = [[] for _ in range(c)]

        for k in range(c):
            for i in range(r):
                res[k].append(matrix[i][k])
        
        return res
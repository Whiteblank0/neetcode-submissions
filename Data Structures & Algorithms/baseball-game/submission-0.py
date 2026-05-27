class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        score = 0

        for op in operations:
            if op == "+":
                score = stack[-1] + stack[-2]
                stack.append(score)
            elif op == 'D':
                score = stack[-1] * 2
                stack.append(score)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        
        return sum(stack)
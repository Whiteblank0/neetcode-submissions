class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {']':'[', '}':'{', ')':'('}

        for char in s:
            if char in dic:
                if not stack or dic[char] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        
        return not stack
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = set()

        for num in nums:
            if num not in dic:
                dic.add(num)
            else:
                return num
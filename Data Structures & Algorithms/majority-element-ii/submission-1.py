class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        target = len(nums) // 3
        res = []

        for num in nums:
            count[num] += 1
            if count[num] > target and num not in res:
               res.append(num)
        
        return res
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        target = len(nums) // 3
        res = set()

        for num in nums:
            count[num] += 1
            if count[num] > target:
               res.add(num)
        
        return list(res)
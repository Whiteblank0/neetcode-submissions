class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        start = 0
        end = min(k, len(nums) - 1)
        table = {}
        
        while end < len(nums):
            for i in range(start, end + 1):
                if nums[i] not in table:
                    table[nums[i]] = 1
                else:
                    return True
            
            start += 1
            end += 1
            table = {}
        
        return False
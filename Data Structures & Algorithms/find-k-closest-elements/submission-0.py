import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) <= k:
            return arr
        
        res = []
        diff = [(abs(num - x), i) for i, num in enumerate(arr)]
        heapq.heapify(diff)
        
        while k > 0:
            element = heapq.heappop(diff)
            res.append(arr[element[1]])
            k -= 1
        
        return sorted(res)
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        pq = []

        for point in points:
            x, y = point[0], point[1]
            dis = x ** 2 + y ** 2
            heapq.heappush(pq, (dis, point))
        
        while k > 0:
            _, point = heapq.heappop(pq)
            ans.append(point)
            k -= 1
        
        return ans
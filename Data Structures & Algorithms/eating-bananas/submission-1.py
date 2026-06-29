import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_time = r
        while l<r:
            mid = l+(r-l)//2
            t = 0
            for i in range(len(piles)):
                t += math.ceil(piles[i]/mid)
            if t>h:
                l = mid+1
            else:
                r = mid
        return l

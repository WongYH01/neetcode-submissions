class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # set L and R to 1 and max piles

        # while L < R
            # get mid
            # timer
            # iterate through piles
                # timer += ceil(pile/mid)
            # check if timer bigger than h
                # move L
            # else
                # return mid

        L, R = 1, max(piles)
        min_rate = R
        while L <= R:
            mid = (L+R)//2
            timer = 0
            
            for curr_pile in piles:
                timer += math.ceil(curr_pile/mid)
            if timer > h:
                L = mid+1
            else:
                min_rate = min(min_rate, mid)
                R = mid-1
        return min_rate


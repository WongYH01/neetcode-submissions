class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # get the max bananas in a pile
        # set L and R as 1 and max
        # set k min to be max bananas +1
        # while L<=R:
            # get mid
            # get the elem in mid
            # temp counter
            # iterate thru piles
                # add to counter the ceiling of pile/mid elem
            # check if the result is bigger than h
                # move L to mid+1
            # else
                # store min in k_min
                # move R to mid-1
        # return k min

        max_banana = max(piles)
        L,R = 1,max_banana
        min_k = max_banana+1
        while L<=R:
            mid = (L+R)//2
            h_counter = 0

            for curr_banana_pile in piles:
                h_counter += math.ceil(curr_banana_pile/mid)

            if h_counter > h:
                L = mid+1
            # elif h_counter < h:
            #     R = mid-1
            else:
                min_k = min(min_k,mid)
                R = mid-1
        return min_k
        

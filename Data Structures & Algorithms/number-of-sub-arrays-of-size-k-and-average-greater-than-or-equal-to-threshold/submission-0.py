class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # set L as 0
        # starting sum of 0
        # res_counter

        # iterate with R
            # check if R is out of bounds
                # check if the current sum is >= threshold
                    # up the counter
                # minus the elem at L
                # move L up
            # add R elem to sum
        # return counter

        L = 0
        counting_sum = 0
        res_counter = 0

        for R in range(len(arr)):
            if R-L+1 > k:
                if counting_sum >= k*threshold:
                    res_counter+=1
                counting_sum-=arr[L]
                L+=1
            counting_sum+=arr[R]
        if counting_sum >= k*threshold:
            res_counter+=1
        return res_counter
        
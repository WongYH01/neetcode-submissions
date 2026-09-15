class Solution:
    def findMin(self, nums: List[int]) -> int:
        # set L and R

        # check if elem at R is bigger than elem at L
            # return elem at L

        # min_res var set to index 0
        # while L <= R
            # get mid
            # bank mid with min

            # check if mid is >= L elem (Scenario where mid is part of larger seq)
                # move L to the right
            # else (Scenario where mid is part of the smaller seq, but might be in the middle/end, SO move left to see!)
                # move R to the left
        # return min

        L, R = 0, len(nums)-1
        
        
        min_res = nums[0]
        while L<=R:
            mid = (L+R)//2
            min_res = min(min_res,nums[mid])

            if nums[R]>nums[L]:
                min_res = min(min_res,nums[L])
                return min_res

            if nums[mid] >= nums[L]:
                L = mid+1
            else:
                R = mid-1
        return min_res

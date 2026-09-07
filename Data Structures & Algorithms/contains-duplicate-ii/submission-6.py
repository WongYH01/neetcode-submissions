class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # L
        # window
        # iterate thru nums with R
            # check if the set is not empty and whether R is in the window
                # return true
            # if curr num is out of the window
                # remove the left one
            # add the curr num to window
        if k == 0:
            return False
        L = 0
        window = set()
        for R in range(len(nums)):
            if window and nums[R] in window:
                return True
            if R-L+1>k:
                window.remove(nums[L])
                L+=1
            window.add(nums[R])
        return False
                

        
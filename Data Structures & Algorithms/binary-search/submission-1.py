class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # set L and R to start and end

        # while L is <= R
            # get mid
            # check if target < mid
                # set R to be mid -1
            # elif target > mid
                # set L to mid +1
            # else means meet target
                # return index
        # return -1

        L,R = 0, len(nums)-1

        while L<=R:
            mid = (L+R)//2

            if target < nums[mid]:
                R = mid-1
            elif target > nums[mid]:
                L = mid+1
            else:
                return mid
        return -1

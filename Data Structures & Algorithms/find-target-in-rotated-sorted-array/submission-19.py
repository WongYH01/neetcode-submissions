class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # set L and R as start and end

        # while L < R
            # get mid

            # check if in the left sorted
                # check if target in between
                    # move R
                # else
                    # move L


            # check if in the right sorted
                # check if target in between
                    # move L
                # else
                    # move R
        L, R = 0, len(nums)-1

        while L <= R:
            mid = (L+R)//2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[L]:
                if nums[L] <= target <= nums[mid]:
                    R = mid-1
                else:
                    L = mid+1
            else:
                if nums[mid] <= target <= nums[R]:
                    L = mid+1
                else:
                    R = mid-1

        return -1
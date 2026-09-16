class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # get L and R
        # while L is <= R
            # check if the mid element is the target
                # return mid index

            # if mid is on the left sorted (elem L <= elem mid)
                # check if target element is in between the left side
                    # move left
                # else
                    # move right
        
            # if mid is on the right sorted
                # check if target element is in between the right side
                    # move right
                # else
                    # move left
        # return -1

        L,R = 0, len(nums)-1
        while L<=R:
            mid = (L+R)//2
            
            if nums[mid] == target:
                return mid
            
            if nums[L] <= nums[mid]:
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

            
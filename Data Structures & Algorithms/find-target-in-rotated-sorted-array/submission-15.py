class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L,R = 0, len(nums)-1
        
        while L<=R:
            mid = (L+R)//2
            mid_nums = nums[mid]
            l_nums,r_nums = nums[L],nums[R]

            if nums[mid] == target:
                return mid
            

            if l_nums <= mid_nums:
                if target >= l_nums and target <= mid_nums:
                    R = mid-1
                else:
                    L = mid+1
            else:
                if target >= mid_nums and target <= r_nums:
                    L = mid+1
                else:
                    R = mid-1
        return -1
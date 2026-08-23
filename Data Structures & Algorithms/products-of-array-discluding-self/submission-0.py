class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # empty array storing products to the RIGHT of indexed number
        # empty array storing products to the LEFT of indexed number

        # set to RIGHT[0] = 1
        # iterate from index 1 to end with i
            # current value of RIGHT to be prev RIGHT and prev num in nums

        # set LEFT[-1] = 1
        # iterate from len-2 to -1 reverse
            # current value of LEFT to be prev LEFT and prev num in nums

        # res array
        # iterate thru to len of nums
            # get the product
            # append to res array
        
        n = len(nums)
        to_right_arr, to_left_arr = [0]*n,[0]*n

        to_right_arr[0]=1
        for i in range(1, n):
            to_right_arr[i] = to_right_arr[i-1] * nums[i-1]
        
        to_left_arr[-1]=1
        for j in range(n-2, -1, -1):
            to_left_arr[j] = to_left_arr[j+1] * nums[j+1]
        
        res_array = []
        for i in range(n):
            res = to_right_arr[i]*to_left_arr[i]
            res_array.append(res)
        
        return res_array
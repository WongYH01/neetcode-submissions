class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        counter = nums[0]
        res_arr = [0]*len(nums)
        res_arr[0]=1

        for i in range(1, len(nums)):
            res_arr[i] = counter
            counter*=nums[i]

        counter_2 = nums[-1]
        for j in range(len(nums)-2,-1,-1):
            res_arr[j]*= counter_2
            counter_2*=nums[j]

        return res_arr

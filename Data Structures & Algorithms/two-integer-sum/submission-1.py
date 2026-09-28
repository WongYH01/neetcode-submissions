class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap
        # iterate nums with index
            # find the difference
            # check if the difference in hashmap
                # return the value and current index
            # set curr elem as key and index as val
        num_map = {}
        for i in range(len(nums)):
            curr_elem = nums[i]
            difference = target-curr_elem

            if difference in num_map:
                return [num_map[difference],i]
            
            num_map[curr_elem] = i
            
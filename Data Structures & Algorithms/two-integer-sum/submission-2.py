class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap
        # iterate thru nums array
            # check if the difference in the hashmap
                # return the value
            # add to hashmap
        num_map = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in num_map:
                return [num_map[remainder], i]
            num_map[nums[i]] = i
        
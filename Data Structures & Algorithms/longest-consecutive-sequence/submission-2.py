class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_counter = 0
        for num in nums_set:
            if (num-1) not in nums_set:
                curr_counter = 1
                curr_num = num
                while curr_num+1 in nums_set:
                    curr_counter += 1
                    curr_num += 1
                if curr_counter > max_counter:
                    max_counter = curr_counter
        return max_counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # curr node = i
        # next node = nums[i]

        # set a slow and fast pointer
        # while the curr nodes are 
            # the next node to be at is the nums[pointer]
            # set the slow pointer to be that
            # set the fast pointer to be the one AFTER that
        
        # (now fast and slow have intersected)

        # set up another pointer at the start
        # while they have not intersected
            # move new pointer and slow by 1
        # return new pointer

        slow,fast = nums[0],nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        new_ptr = 0
        while new_ptr != slow:
            new_ptr = nums[new_ptr]
            slow = nums[slow]
        
        return new_ptr
        

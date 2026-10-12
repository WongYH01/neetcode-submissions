class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # slow and fast pointer 2 nodes ahead using elem as index to go

        # while the slow and fast pointer have not intercepted
            # move slow by 1
            # move fast by 2
        
        # set a slower node as 0
        # while the new slow node not the same as old slow node
            # move slow by 1
            # move new slow by 1
        
        # return the elem using the slow index

        slow, fast = nums[0], nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow_2 = 0
        while slow != slow_2:
            slow = nums[slow]
            slow_2 = nums[slow_2]
        
        return slow_2
        


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap array
        # heapify it

        # iterate thru nums array
            # push number into heap

            # while the length of heap is bigger than k
                # pop
        
        # return the popped
        heap = []
        heapq.heapify(heap)

        for num in nums:
            heapq.heappush(heap, num)

            while len(heap) > k:
                heapq.heappop(heap)
        
        return heapq.heappop(heap)
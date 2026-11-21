class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # convert stone array to neg
        # turn into heap

        # while the length of arr is more than 1
            # set y to be first pop converted to pos
            # set x to be 2nd pop converted to pos

            # check if x < y
                # take the diff
                # push back into heap
            
        # set res to 0
        # check if heap exists
            # set res to first elem
        # return res

        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            y = heapq.heappop(max_heap) * -1
            x = heapq.heappop(max_heap) * -1

            if x < y:
                diff = (y-x)
                heapq.heappush(max_heap, -diff)
        
        res = 0
        if max_heap:
            res = -heapq.heappop(max_heap)
        
        return res

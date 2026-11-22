from _heapq import heapify
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # make an array
        # heapify it

        # iterate thru array of points
            # get the distance using euclidean making it negative
            # format into a tuple
            # push tuple into heap

            # while the length of heap exceeds k
                # pop 
        
        # res array
        # while the heap still exists
            # pop
            # format it properly
            # append to res array
        
        # return res array

        heap = []
        heapq.heapify(heap)

        for curr_pt in points:
            x, y = curr_pt[0],curr_pt[1]
            dist = ((x**2 + y**2)**0.5) * -1
            fmt = (dist,x,y)

            heapq.heappush(heap,fmt)

            while len(heap) > k:
                heapq.heappop(heap)
        
        res_arr = []
        while heap:
            curr = heapq.heappop(heap)
            fmt = [curr[1],curr[2]]
            res_arr.append(fmt)
        
        return res_arr

         
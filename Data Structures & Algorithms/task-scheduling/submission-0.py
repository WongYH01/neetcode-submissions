class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # iterate thru values in Counter
            # push negative vals into heap
    
        # empty deque()
        # timer start from 1

        # while the heap is not empty or queue is not empty
            # check if heap got stuff
                # store pop in var
                # set remainder to be var + 1

                # check if the remainder < 0
                    # fmt it [remainder,next timer]
                    # append to queue
            
            # check if queue got stuff and index 1 of peek same as timer
                # pop
                # push popped to heap
            
            # up the timer
        # return timer

        heap = []
        for val in Counter(tasks).values():
            heap.append(-val)
        heapq.heapify(heap)

        queue = deque()
        timer = 0

        while heap or queue:
            if heap:
                curr_counter = heapq.heappop(heap)
                remain_counter = curr_counter + 1

                if remain_counter < 0:
                    next_timer = timer + n
                    fmt = (remain_counter,next_timer)
                    queue.append(fmt)
            
            if queue and queue[0][1] == timer:
                popped = queue.popleft()
                heapq.heappush(heap,popped[0])
                
            timer += 1
        
        return timer


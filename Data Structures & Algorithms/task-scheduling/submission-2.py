class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # empty arr
        # heapify to max heap

        # iterate thru the values in counters
            # push value into heap
        
        # res time
        # empty queue
        # while heap or queue have stuff
            # check if heap have stuff
                # store popped
                # check if pop - 1 > 0
                    # format it with pop-1, time + n
                    # append to queue
            
            # check if index 1 of queue[0] is the same as time
                # popleft
                # take index 0 of popped and push into max heap
            
            # up counter
        
        # return counter + 1

        heap = []
        heapq.heapify_max(heap)

        for count in Counter(tasks).values():
            heapq.heappush_max(heap,count)
        
        time = 0
        queue = deque()

        while heap or queue:
            if heap:
                heap_pop = heapq.heappop_max(heap)
                if heap_pop-1 > 0:
                    fmt = (heap_pop-1,time+n)
                    queue.append(fmt)
            
            if queue and queue[0][1] == time:
                queue_pop = queue.popleft()
                heapq.heappush_max(heap,queue_pop[0])
            
            time += 1
        
        return time
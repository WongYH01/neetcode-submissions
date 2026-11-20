class KthLargest:
    # push helper function taking the heap and val arg
        # append to end of heap array
        # set index of the new val post as i

        # while elem root of i (i//2) > elem i
            # temp var to store root elem
            # replace root index with elem of i
            # replace remainder with temp var
    def push(self, val):
        self.min_heap.append(val)
        curr_idx = len(self.min_heap)-1

        while self.min_heap[curr_idx//2] > self.min_heap[curr_idx] and curr_idx > 1:
            tmp = self.min_heap[curr_idx//2]
            self.min_heap[curr_idx//2] = self.min_heap[curr_idx]
            self.min_heap[curr_idx] = tmp

            curr_idx = curr_idx//2

    # pop helper function
        # check if min heap length 1
            # return None
        # check if min heap length 2
            # return the array pop
        
        # set res to be index 1
        # replace index 1 with the array pop
        # set curr index to be 1

        # while index left exists (curr_index*2 < len(min_heap))
            # check if index right exists + elem of right is smaller than root and left
                # swap w/ temp root and right
            # elif elem at left is smaller than root
                # swap w/ temp root and left
            # else
                # break out of loop

        # return the res
    def pop(self):
        min_heap = self.min_heap
        if len(min_heap) == 1:
            return None
        if len(min_heap) == 2:
            return min_heap.pop()
        
        res = min_heap[1]
        min_heap[1] = min_heap.pop() 
        curr_idx = 1

        while curr_idx*2 < len(min_heap):
            left_idx = curr_idx*2
            right_idx = curr_idx*2+1
            if (right_idx < len(min_heap)) and (min_heap[right_idx] < min_heap[curr_idx]) and (min_heap[right_idx] < min_heap[left_idx]):
                tmp = min_heap[curr_idx]
                min_heap[curr_idx] = min_heap[right_idx]
                min_heap[right_idx] = tmp
                curr_idx = right_idx
            elif (min_heap[left_idx] < min_heap[curr_idx]):
                tmp = min_heap[curr_idx]
                min_heap[curr_idx] = min_heap[left_idx]
                min_heap[left_idx] = tmp
                curr_idx = left_idx
            else:
                break
        return res

    def __init__(self, k: int, nums: List[int]):
        self.limit = k
        self.min_heap = [0]

        for num in nums:
            self.push(num)
        

    def add(self, val: int) -> int:
        self.push(val)

        # check if the length of min heap exceeds limit
            # get the diff
            # iterate diff with i
                # pop
        # return index 1
        if (len(self.min_heap)-1) > self.limit:
            diff = (len(self.min_heap)-1) - self.limit
            for i in range(diff):
                self.pop()
        return self.min_heap[1]

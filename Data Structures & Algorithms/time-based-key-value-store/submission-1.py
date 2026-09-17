class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # key-value (name:[(value, timestamp),(value, timestamp),(value, timestamp)])
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        # min_key_index
        
        # get L and R index
        # while L<=R
            # find mid
            # get mid details
            # check if mid timestamp is smaller than target
                # check if mid timestamp bigger than min_key_index timestamp
                    # replace with mid index
                # move to the right
            # elif mid timestamp bigger than target
                # move to the left
            # else
                # return the value
        # return the value of the min_key_index

        if key not in self.time_map:
            return ""
        
        curr_array = self.time_map[key]
        L,R = 0,len(curr_array)-1
        closest_value = ""

        while L <= R:
            mid = (L+R)//2
            mid_timestamp = curr_array[mid][0]
            mid_value = curr_array[mid][1]
        
            if mid_timestamp < timestamp:
                closest_value = mid_value
                L = mid+1
            elif mid_timestamp > timestamp:
                R = mid-1
            else:
                return mid_value
        return closest_value


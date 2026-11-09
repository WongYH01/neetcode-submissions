class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums hash map
        # iterate thru nums array
            # check if got no key
                # add to key w/ value of 0
            # add 1 to the value
        
        # spawn an array w/ arrays count to len of nums
        # iterate thru the hashmap
            # set array index as the value 
        
        nums_map = {}
        for num in nums:
            if num not in nums_map:
                nums_map[num] = 0
            nums_map[num] += 1


        counter_arr = []
        for i in range(len(nums)+1):
            tmp = []
            counter_arr.append(tmp)
        # [[],[],[],[]]
        for val,freq in nums_map.items():
            counter_arr[freq].append(val)


        res_arr = []
        limit = 0
        for count_arr in counter_arr[::-1]: 
            for num in count_arr[::-1]:
                res_arr.append(num)
                limit += 1
                if limit == k:
                    return res_arr
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # ref hash map
        # iterate thru nums
            # check if key not in hashmap
                # create a new key with value of 0
            # add 1 to the value

        # create a list of lists where each index is the count

        # iterate hashmap
            # use the val as index
            # append the key to list
        
        # counter
        # res list

        # iterate list backwards
            # check curr list is not empty
                # up the counter
                # concat list to res list
                # check if counter becomes k
                    # return res list
        
        nums_map = {}
        for num in nums:
            if num not in nums_map:
                nums_map[num]=0
            nums_map[num]+=1
        
        bucket_list = []
        for i in range(len(nums)+1):
            tmp = []
            bucket_list.append(tmp)

        for key,val in nums_map.items():
            bucket_list[val].append(key)
        
        counter = 0
        res_list = []
        for curr_count_arr in bucket_list[::-1]:
            # if curr_count_arr:
            #     res_list+=curr_count_arr
            #     counter+=1
            #     if counter == k:
            #         break
            for el in curr_count_arr:
                res_list.append(el)
                if len(res_list) == k:
                    return res_list
        return res_list


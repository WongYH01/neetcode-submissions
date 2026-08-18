class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        # empty dict
        # iterate thru list of ints
            # check if num exist in dict
                # +=1 the value
            # else
                # new key with value of 1
        
        # generate a list of empty lists up to the length of the list
        # iterate thru dict
            # append the list with key based on value index
        
        # res array
        # iterate thru the list backwards
            # if curr array len more than 0
                # append to array
                # up the counter
                # if counter == k
                    # return the res array

        freq_dict = {}
        for curr_num in nums:
            if curr_num in freq_dict:
                freq_dict[curr_num] += 1
            else:
                freq_dict[curr_num] = 1
        
        # return freq_dict
        bucket_list = [[] for _ in range(len(nums)+1)]

        for num,count in freq_dict.items():
            bucket_list[count].append(num)
        
        res_array = []
        curr_counter = 0
        for count in bucket_list[::-1]:
            if len(count)>0:
                res_array+=count
                curr_counter += len(count)
            if curr_counter == k:
                return res_array

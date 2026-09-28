class Solution:
    # helper function to convert word to bucket sort
    def convert_to_bucket(self, word):
        # create a list of 26 0s
        # iterate thru every char of word
            # get the index with ord('a')-ord(char)
            # +=1 the index of bucket list
        # convert bucket list to tuple and return
        bucket_list = []
        for i in range(26):
            bucket_list.append(0)
        
        for char in word:
            insert_index = ord('a')-ord(char)
            bucket_list[insert_index] +=1
        
        return tuple(bucket_list)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash map
        # iterate thru list of strs
            # use helper function to convert word to bucket sort
            # check if the set does not exist in hash map
                # set a new key with val of empty array
            # append word to array value
        str_map = {}
        for curr_str in strs:
            bucket_tuple = self.convert_to_bucket(curr_str)
            if bucket_tuple not in str_map:
                str_map[bucket_tuple] = []
            str_map[bucket_tuple].append(curr_str)

        res_list = []
        for key, val in str_map.items():
            res_list.append(val)
        
        return res_list
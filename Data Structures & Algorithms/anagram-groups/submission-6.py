class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap
        
        # iterate thru the strings
            # temp array w/ 26 indexes
            # iterate thru each char
                # get the index by char - ord('a')
                # temp array[index]+=1
            # convert to set
            # check if in hashmap
                # add a key w/ value of empty array
            # append string into value array
        
        # res array
        # iterate thru hashmap
            # append to res array
        
        # return res array

        bucket_map = {}

        for curr_str in strs:
            tmp_arr = [0]*26
            for char in curr_str:
                index = ord(char) - ord('a')
                tmp_arr[index] += 1
            
            setted = tuple(tmp_arr)
            if setted not in bucket_map:
                bucket_map[setted] = []
            bucket_map[setted] += [curr_str]
        
        res_arr = []
        for buck in bucket_map:
            res_arr.append(bucket_map[buck])
        
        return res_arr






class Solution:
    def helper(self, inp_str:str):
        # new list with 26 empty elements of 0
        # iterate thru chars in string
            # get the position with ord(char) - ord('a')
            # one up the curr index
        arrayer = [0]*26
        for char in inp_str:
            char_post = ord(char)-ord('a')
            arrayer[char_post] += 1
        tupler = tuple(arrayer)
        return tupler

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # empty dict
        # iterate thru list of strings
            # run helper function
            # check whether in dict alrdy
                # append the word to value
            # else
                # new array w/ str as value then put key
        
        # res array
        # iterate thru dict keys
        # append value into array

        dicter = {}
        for curr_str in strs:
            curr_freq_count = self.helper(curr_str)
            if curr_freq_count in dicter:
                dicter[curr_freq_count].append(curr_str)
            else:
                dicter[curr_freq_count] = [curr_str]
        
        res_array = []
        for dict_keys in dicter.keys():
            res_array.append(dicter[dict_keys])
        return res_array



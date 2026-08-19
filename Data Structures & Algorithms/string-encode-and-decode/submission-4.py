class Solution:

    def encode(self, strs: List[str]) -> str:
        # empty string
        # iterate thru list of strings
            # get the length
            # concat length, delimeter and word to string
        # return the string
        encoded_array = [f"{len(curr_string)}#{curr_string}" for curr_string in strs]
        encoded_string = "".join(encoded_array)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        # res array
        # set j as 0
        # iterate thru string with i
            # check if the current char is #
                # retreive the length w/ slicing between j and i
                # get the string slice starting at i and ending at i + length
                # append the string to array
                # move i and j to the next word
        res_array = []
        j = 0
        i = 0
        while i < len(s):
            if s[i] == "#":
                length = int(s[j:i])
                string_found = s[i+1:i+1+length]
                res_array.append(string_found)
                i = i+1+length
                j = i
            else:
                i+=1
        return res_array

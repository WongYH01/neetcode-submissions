class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Set left to start, right to length
        # while the right is bigger than the left
            # check if the curr elem is not an alphanum
                # move
            # check if the now elem is not the same
                # false
            # up L, down R
        new_s = ""
        for char in s:
            if char.isalnum():
                new_s += char.lower()

        L, R = 0, len(new_s)-1
        while R>L:
            if new_s[L] != new_s[R]:
                return False
            L += 1
            R -= 1
        return True

        
        
class PrefixNode:
    def __init__(self) -> None:
        # set attr of hashmap containing children
        # set attr on whether its end of word
        self.children = {}
        self.end_word = False

class PrefixTree:

    def __init__(self):
        # a new PrefixNode
        self.root = PrefixNode()
        

    def insert(self, word: str) -> None:
        # iterate char of word
            # check if it does not exists in children hashmap
                # make a key with Node as value
            # move pointer to next
        # set the last char to last word
        curr_root = self.root
        for c in word:
            if c not in curr_root.children:
                curr_root.children[c] = PrefixNode()
            curr_root = curr_root.children[c]
        curr_root.end_word = True


    def search(self, word: str) -> bool:
        # iterate thru word
            # check if char does not exist in children
                # return False
            # move the pointer
        # return the last word 
        curr_root = self.root
        for c in word:
            if c not in curr_root.children:
                return False
            curr_root = curr_root.children[c]
        return curr_root.end_word
        

    def startsWith(self, prefix: str) -> bool:
        # iterate thru prefix
            # check if char is not in children
                # return false
            # move the pointer
        # return True
        curr_root = self.root
        for c in prefix:
            if c not in curr_root.children:
                return False
            curr_root = curr_root.children[c]
        return True


        
        
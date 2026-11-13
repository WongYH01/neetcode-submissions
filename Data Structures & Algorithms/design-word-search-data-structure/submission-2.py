class WordNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_word = False


class WordDictionary:

    def __init__(self):
        self.root = WordNode()
        

    def addWord(self, word: str) -> None:
        curr_root = self.root
        for c in word:
            if c not in curr_root.children:
                curr_root.children[c] = WordNode()
            curr_root = curr_root.children[c]
        curr_root.end_word = True
        

    def search(self, word: str) -> bool:

        def dfs(start_index, curr_node):
            
            curr_root = curr_node

            for i in range(start_index,len(word)):
                c = word[i]
                # .ab
                if c == ".":
                    for child_node in curr_root.children.values():
                        if dfs(i+1,child_node):
                            return True
                    return False
                else:
                    if c not in curr_root.children:
                        return False
                    curr_root = curr_root.children[c]
            return curr_root.end_word
        
        return dfs(0, self.root)
        


            
            
            
            
            
        

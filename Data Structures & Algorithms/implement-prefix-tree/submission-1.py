class PrefixNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        curr_root = self.root

        for c in word:
            if c not in curr_root.children:
                curr_root.children[c] = PrefixNode()
            curr_root = curr_root.children[c]
        curr_root.word = True


    def search(self, word: str) -> bool:
        curr_root = self.root

        for c in word:
            if c not in curr_root.children:
                return False
            curr_root = curr_root.children[c]
        return curr_root.word

    def startsWith(self, prefix: str) -> bool:
        curr_root = self.root

        for c in prefix:
            if c not in curr_root.children:
                return False
            curr_root = curr_root.children[c]
        return True
        
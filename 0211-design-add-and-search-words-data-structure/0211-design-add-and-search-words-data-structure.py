class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        node = self.trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["$"] = True            

    def search(self, word: str) -> bool:

        def dfs(node, idx):

            if idx == len(word):
                return "$" in node

            ch = word[idx]
            if ch == '.':

                for child in node:
                    if child != "$" and dfs(node[child], idx + 1):
                        return True
                return False
        
            
            if ch in node:
                return dfs(node[ch], idx + 1)
            return False

        return dfs(self.trie, 0)


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
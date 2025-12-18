from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # Understood the logic and the DFS, BFS part but struggled in finding the replacement code like
        # changing each word character from a to z and checking in list. Used new syntax for it.

        word_list = set(wordList)
        if endWord not in word_list:
            return 0

        q  = deque([(beginWord, 1)])

        while q:

            word, steps = q.popleft()
            if word == endWord:
                return steps
            

            for i in range(len(word)):
                orig = word[i]
                for char in string.ascii_lowercase:
                    if char == orig:
                        continue
                    newWord = word[:i] + char + word[i+1:]
                    if newWord in word_list:
                        q.append((newWord, steps+1))
                        word_list.remove(newWord)
                

        return 0
            


        



                  




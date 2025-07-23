class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # recursive function dfs to check through each letter
        
        # go through each i,j:
        #     start dfs with i,j when it matches the first word
        # dfs func:
        #     if last letter in the word:
        #         return true
        # 
        #     if mismatch return false    
        # 
        #     put curr in temp and replace it wiht specila char
        # make 4 calls in 4 directions

        # if mismatch backtrack 
        #  i,j back to temp val
        length = len(word)

        def dfs(i,j,idx):
            
            if len(word) == idx:
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[idx]:
                return False
            if board[i][j] == word[idx]:
                temp = board[i][j]
                board[i][j] = '$'

                res = dfs(i+1,j,idx+1) or dfs(i-1,j,idx+1) or dfs(i,j+1,idx+1) or dfs(i,j-1,idx+1) 

                board[i][j] = temp

                return res


        res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False








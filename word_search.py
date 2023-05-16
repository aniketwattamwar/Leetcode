board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = ["ABCB"]
visited = set()

def dfs(r,c,i):

    if i == len(word):
        print(True)
    if r < 0 or c < 0 or r>=len(board) or c>= len(board[0]) or word[i] != board[r][c] or (r,c) in visited:
        print(False)
    visited.add((r,c))

    res = ( dfs(r+1,c,i+1) or 
            dfs(r,c+1,i+1) or 
            dfs(r-1,c,i+1) or
            dfs(r,c-1,i+1))
    visited.remove((r,c))
    print(res)


for r in range(len(board)):
    for c in range(len(board[0])):
        if dfs(r,c,0):
            print( True)

print(False)
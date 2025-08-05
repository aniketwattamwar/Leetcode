class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # thhe logic was simple and code also easy
        # just few edge cases to check and decision to do it from right to left
#       saw the code for reverse start from right to left
        m = len(boxGrid)
        n = len(boxGrid[0])
        for row in boxGrid:
            right = n-1
            for col in reversed(range(n)):
                if row[col] == '*':
                    right = col -1 
                elif row[col] == '#':
                    if col != right:
                        row[right], row[col] = row[col], '.'
                    right -=1
            
        # easy but struggled to rotate
        rotated = [[None] * m for _ in range(n)]  # saw this line
        for i in range(m):
            for j in range(n):
                rotated[j][m-1-i] = boxGrid[i][j]

        return rotated


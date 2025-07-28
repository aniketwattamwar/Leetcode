class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        # use dfs to make the substrings
        #  Check if palindrome or not. If yes add to final answer list
        
        # Got the logic and solution. Use subsets problem just add logic if subset 
        # is palindrome or not

        result = []
        palindrome_subset = []

        def isPalindrome(s,i,j):
            temp = s[i:j+1]

            return temp == temp[::-1]
        
        def dfs(i):
            if i >= len(s):
                result.append(palindrome_subset.copy())
                return
            for j in range(i,len(s)):
                if isPalindrome(s,i,j):
                    palindrome_subset.append(s[i:j+1])
                    dfs(j + 1)
                    palindrome_subset.pop()

        dfs(0)
        return result
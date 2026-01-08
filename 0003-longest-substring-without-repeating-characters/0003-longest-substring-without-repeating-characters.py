class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        mapping = {}
        n = len(s)
        ans , i = 0, 0
        for j in range(n):
            if s[j] in mapping:
                i = max(mapping[s[j]], i)

            ans = max(ans, j - i + 1)
            mapping[s[j]] = j + 1
        return ans 
        
        
        
        # create all substrings 
        # store all them in a list
        # calculate its lenght and keep track of the maximum leng
        # return max length

        # n = len(s)
        # maxLen = 0
        # for i in range(n):
        #     temp = ""
        #     for j in range(i,n):
        #         if s[j] not in temp:
        #             temp += s[j]
        #     print(temp)
        #     maxLen = max(maxLen, len(temp))
                
        # return maxLen
            




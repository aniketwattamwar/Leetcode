#     # Problem 3
    
# def lengthOfLongestSubstring(s):
    
#     start = m_len = 0
#     d = {}
    
#     for i in range(len(s)):
#         if s[i] in d and start <= d[s[i]]:
#             start = d[s[i]] + 1
#         else:
#             m_len = max(m_len,i - start + 1)
    
#         d[s[i]] = i
        
#     return m_len


# ans = lengthOfLongestSubstring("abcabcbb")
# print(ans)

s = "au"
l = 0
r = 0
n = len(s)
d = {}
m = 0
length = 0
while l < n and r < n:
            
    if s[r] not in d:
        d[s[r]]=1
        r+=1
    else:
        l+=1
        r = l
        length = len(d)
        d = {}
    if m < length:
        m = length

print(m)

















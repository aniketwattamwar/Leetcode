    # Problem 3
    
def lengthOfLongestSubstring(s):
    
    start = m_len = 0
    d = {}
    
    for i in range(len(s)):
        if s[i] in d and start <= d[s[i]]:
            start = d[s[i]] + 1
        else:
            m_len = max(m_len,i - start + 1)
    
        d[s[i]] = i
        
    return m_len


ans = lengthOfLongestSubstring("abcabcbb")
print(ans)
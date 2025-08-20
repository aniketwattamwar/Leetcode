from collections import Counter 
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        
        freq_p = Counter(p)
        print(freq_p)
        res = []
        for i in range(len(s)):
            substr = s[i:i+len(p)]
            freq_substr = Counter(substr)
            print(freq_substr)
            if freq_substr == freq_p:
                res.append(i)
        return res



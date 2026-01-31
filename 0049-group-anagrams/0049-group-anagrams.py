from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)
        for word in strs:
            temp = []
            for ch in word:
                temp.append(ch)
            # print(temp)                
            temp_sorted = tuple(sorted(temp))
            if d[temp_sorted]:
                d[temp_sorted].append(word)
            else:
                d[temp_sorted] = [word]
        # print(d)

        return list(d.values())
        



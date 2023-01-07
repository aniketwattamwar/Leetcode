import collections

def groupAnagrams(strs):
        
        ## Easy problem to understand and come up with a logic. But difficult to code it up. Saw the below solutio and learned a new way to use collections. Interesting solution.
        ## Another solution is to create a key with 26 letters. The words with the same letters will have same key like 1 0 0 0 0 1 0..... like this.

        ans = []
        mapping = defaultdict(list)
        for s in strs:
            a = []
            a = sorted(s)            
            mapping[tuple(a)].append(s)
    
        for m in mapping.values():
            ans.append(m)
        
        print(ans)
        print(sorted(strs))
        print(mapping)

        return ans
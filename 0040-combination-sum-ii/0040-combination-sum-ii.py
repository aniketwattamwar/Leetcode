class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combination = []
        res = []
        candidates.sort()
        def rec(i, combination, total):
            if target == total:
                res.append(combination.copy())
                return
            if target < total or i == len(candidates) :
                return
            
            combination.append(candidates[i])
            # print(combination)
            # rec(i, combination, total + candidates[i])
            rec(i+1,combination, total+candidates[i])
            combination.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1

            rec(i+1, combination, total)
            
        rec(0,[],0)
        return res
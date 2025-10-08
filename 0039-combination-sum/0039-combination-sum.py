class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

        combination = []
        res = []
        def rec(i, combination, total):
            if i >= len(candidates) or target < total:
                return
            if target == total:
                res.append(combination.copy())
                return
            combination.append(candidates[i])
            rec(i, combination, total + candidates[i])
            combination.pop()
            rec(i+1,combination, total)
        rec(0,[],0)
        return res


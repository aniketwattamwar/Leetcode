class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        
        jobs = sorted(jobs, reverse= True)

        arr = [0]*k
        best_time = float('inf')
        

        def backtrack(jobs, idx, arr):
            nonlocal best_time
            if idx == len(jobs):
                curr_max = max(arr)
                best_time = min(curr_max, best_time) # a little confusing returning the minimum of all maximums???
                return

            if max(arr) >= best_time:
                return
            
            for i in range(len(arr)):
                
                if i > 0 and arr[i] == arr[i - 1]:
                    continue
                

                if arr[i] + jobs[idx] >= best_time:
                    continue
                
                arr[i]+=jobs[idx]
                backtrack(jobs, idx+1, arr)
                arr[i] -= jobs[idx]
            

        backtrack(jobs,0, arr)

        return best_time





from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        mapping = defaultdict(list)
        for i in range(len(prerequisites)):
            course, pre = prerequisites[i]
            if course not in mapping:
                mapping[course] = [pre]
            else:
                mapping[course].append(pre) 
        

        visited = [0]*numCourses
        def dfs(course):
            if visited[course] == -1:
                return False
            if visited[course] == 1:
                return True
            visited[course] = -1
            for pre in mapping[course]:
                if not dfs(pre):
                    return False
            visited[course] = 1
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False


        return True
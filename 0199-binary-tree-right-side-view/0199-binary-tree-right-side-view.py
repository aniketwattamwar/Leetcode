# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = deque([root])
        final_ans = []
        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            final_ans.append(level[-1])


        return final_ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if root is None:
        #     return []
        # q = [root]
        # nq = []
        # level = []
        # ans = []
        # while q!=[]:
        #     for node in q:
        #         level.append(node.val)
        #         if node.left:
        #             nq.append(node.left)
        #         if node.right:
        #             nq.append(node.right)
                
        #     print(level)
        #     ans.append(level[-1])
        #     level = []
        #     q = nq 
        #     nq = []

        # print(ans)
        # return ans


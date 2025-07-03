# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def dfs(root,h):
            if root is None:
                return h
            
            lh = dfs(root.left, h+1)
            rh = dfs(root.right, h+1)
            
            return max(lh,rh)

        return 1 + max(dfs(root.left,0),dfs(root.right,0))
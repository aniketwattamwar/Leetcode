# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        if not root:
            return 0
        
        def dfs(root, currMax):
            nonlocal count
            if root is None:
                return 
            if currMax <= root.val:
                currMax = root.val
                count+=1
            dfs(root.left,currMax)
            dfs(root.right,currMax)
            return count
        
        final_count = dfs(root, root.val)
        return final_count




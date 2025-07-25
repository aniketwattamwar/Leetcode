# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p,q):
           
            if p is None and q is None:
                return True 
            if (p and not q) or (q and not p):
                return False
            if p and q and p.val == q.val:
                return (isSameTree(p.left, q.left) and isSameTree(p.right,q.right))
            
            return False
            
        if not subRoot:
            return True
        if not root:
            return False
            
        if isSameTree(root,subRoot):
            return True


        return (self.isSubtree(root.left,subRoot) or
        self.isSubtree(root.right,subRoot))
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        l =[]

        def inorder(root):
            if root is None:
                return

            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
        inorder(root)
        if sorted(set(l)) == l:
            return True
        return False
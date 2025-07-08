# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # l = []
        # def inorder(root):
        #     if root is None:
        #         return None
        #     inorder(root.left)
        #     l.append(root.val)
        #     inorder(root.right)


        # inorder(root)
        # return l[k-1]

        cnt = k
        ans = 0
        def inorder(root):
            nonlocal cnt, ans
            if root is None: return None
            
            inorder(root.left)
            cnt-=1
            if cnt == 0:
                ans = root.val
                return 
            inorder(root.right)
        inorder(root)
        return ans
        
        
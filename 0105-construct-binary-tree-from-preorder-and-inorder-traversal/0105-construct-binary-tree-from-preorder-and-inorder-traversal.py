# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        
        # Undderstood the logic but was not able to code it up
        # below is neetcode solution
        hashmap = {}
        self.idx = 0
        for i,v in enumerate(inorder):
            hashmap[v] = i
        print(hashmap)
        def dfs(l,r):
            if l>r:
                return None
            val = preorder[self.idx]
            self.idx+=1
            root = TreeNode(val)
            m = hashmap[val]
            root.left = dfs(l,m-1)
            root.right = dfs(m+1,r)
            return root
        
        return dfs(0,len(inorder)-1)
            
            
            



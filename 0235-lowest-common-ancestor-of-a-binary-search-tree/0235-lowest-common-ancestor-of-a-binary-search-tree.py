# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        all_nodes=[]
        def traverse_till_node(root, node):
            all_nodes.append(root.val)
            if root.val == node.val:
                return all_nodes
            if root.val > node.val:
                return traverse_till_node(root.left, node)
                 
            else:
                return traverse_till_node(root.right, node)
                
            

        till_p = traverse_till_node(root, p)
        all_nodes = []
        till_q = traverse_till_node(root, q)

        lp = len(till_p) 
        lq = len(till_q)
        
        if lp < lq:
            while lp < lq:
                till_p.append(till_p[-1])
                lp +=1 
        elif lp > lq:
            while lp > lq:
                till_q.append(till_q[-1])
                lq+=1
        print(till_p)
        print(till_q)

        
        for i in range(len(till_p)-1,-1,-1):
            if till_p[i] == till_q[i]:
                return TreeNode(till_p[i])




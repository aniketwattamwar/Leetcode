# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def rserialize(root, string):
            if root is None:
                string += "None,"
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string

        return rserialize(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(string):
            if string[0] == 'None':
                string.pop(0)
                return None
            root = TreeNode(string[0])
            string.pop(0)
            root.left = rdeserialize(string)
            root.right = rdeserialize(string)
            return root

        l = data.split(',')
        root = rdeserialize(l)

        return root
        




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
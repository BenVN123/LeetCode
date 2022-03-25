# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def f(node):
            if not node: return (None, None)
        
            b1, e1 = f(node.left)
            b2, e2 = f(node.right)
            node.left = None
            
            if not e1 and not e2:
                return (node, node)
            
            if not e1 and e2:
                node.right = b2
                return (node, e2)
            
            if e1 and not e2:
                node.right = b1
                return node, e1
            
            else:
                node.right = b1
                e1.right = b2
                return (node, e2)
        
        f(root)
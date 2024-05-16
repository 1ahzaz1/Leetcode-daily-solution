# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        if not root.left and not root.right: #Checking leaf node
            return root.val == 1 #Return True for 1 and False for 0
        
        elif root.val == 2: #Return recursive OR of left and right
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        else: #Return recursive AND of left and right
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
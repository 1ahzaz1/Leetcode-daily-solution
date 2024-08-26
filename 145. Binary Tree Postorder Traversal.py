# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        #iterative solution

        visited = [False]
        mystack = [root]
        output = []

        while mystack:
            curr, val = mystack.pop(), visited.pop()
            if curr:
                if val: #Already seen once
                    output.append(curr.val)
                else:
                    mystack.append(curr)
                    visited.append(True) #seen once
                    mystack.append(curr.right)
                    visited.append(False)
                    mystack.append(curr.left)
                    visited.append(False)
        return output
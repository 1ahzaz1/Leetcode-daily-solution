# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def dfs(node): #post-order dfs search
            if not node: #base case
                return 0

            left_balance = dfs(node.left) #recursive
            right_balance = dfs(node.right)

            balance = node.val - 1 + left_balance + right_balance #Adjusts for moves already made by child nodes

            self.moves += abs(left_balance) + abs(right_balance) #Number of out and in(using abs) moves to reach 1 

            return balance 

        dfs(root)
        return self.moves
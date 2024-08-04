# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.pairs = 0  #our output
        #we will search through the tree and compare each leafs distance to its first common ancestor
        #if the distance is <=1, we increment pairs variable

        def dfs(node):
            if not node: #We searched a nonexistent node
                return []
            if not node.left and not node.right: #We reached a leaf node
                return [1]

            left_distance = dfs(node.left)
            right_distance = dfs(node.right)

            for dist1 in left_distance:
                for dist2 in right_distance:
                    if dist1 + dist2 <= distance:
                        self.pairs +=1
            
            #In the parent node from which right and left were calculated;
            # both these distances come from the same direction
            total_distance = left_distance + right_distance
            #Every time we go up a level to parent, distance from all leaves are incremented
            return [dist+1 for dist in total_distance]
        
        dfs(root)
        return self.pairs
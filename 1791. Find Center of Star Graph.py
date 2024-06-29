class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        x1 = edges[0][0]
        x2 = edges[0][1]
        x1True = True

        #the center node must be one of these 2

        for x,y in edges:
            if x1!=x and x1!=y:
                x1True = False

        #if x1 did not appear in both nodes at any edge, then x2 was the centre
        return x1 if x1True else x2


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (True, float("inf"), float("-inf"))
            if not (node.left or node.right):
                return (True, node.val, node.val) # isBST, min, max
            
            isValidRight, minRight, maxRight = dfs(node.right)
            isValidLeft, minLeft, maxLeft = dfs(node.left)
            
            isValidNode = (isValidRight and isValidLeft) and (maxLeft < node.val < minRight)
            return (isValidNode, min(node.val, minLeft), max(node.val, maxRight))
        
        return dfs(root)[0]

        
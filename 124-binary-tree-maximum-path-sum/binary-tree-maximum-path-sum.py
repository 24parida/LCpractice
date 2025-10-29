# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(node):
            if not node:
                return 0, float('-inf')
            
            right_no, right_split =  dfs(node.right)
            left_no, left_split = dfs(node.left)


            no_split = node.val + max(0, right_no, left_no)
            split_here = node.val + max(0, right_no) + max(0, left_no)
            split = max(split_here, right_split, left_split)

            return (no_split, split)
        
        return max(dfs(root))
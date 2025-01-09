# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def find_sum(node, add):
            if not node: return False
            addition = node.val + add
            if not (node.right or node.left):
                if addition == targetSum:
                    return True
                else:
                    return False
            
            return find_sum(node.right, addition) or find_sum(node.left, addition)
        return find_sum(root, 0)

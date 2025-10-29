# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(left, right):
            if left > right:
                return [None]
            
            res = []
            for i in range(left, right+1):
                leftT = helper(left, i-1)
                rightT = helper(i+1, right)
                for l in leftT:
                    for r in rightT:
                        res.append(TreeNode(i, l, r))
            
            return res
        return helper(1, n)
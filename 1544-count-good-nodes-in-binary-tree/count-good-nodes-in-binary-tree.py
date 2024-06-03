# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global res
        res = 0
        def dfs(n, maxV):
            global res
            if not n: 
                return 
            if n.val >= maxV: res +=1
            dfs(n.left, max(maxV, n.val))
            dfs(n.right, max(maxV, n.val))
        
        dfs(root, root.val)
        return res
        
        
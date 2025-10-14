# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = collections.deque([root])
        res = []
        while q:
            rightMost = None
            for _ in range(len(q)):
                node = q.popleft()
                if node != None:
                    rightMost = node
                    q.append(node.left)
                    q.append(node.right)
            
            if rightMost:
                res.append(rightMost.val)

        return res



        
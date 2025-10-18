# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        column_map = collections.defaultdict(list)
        q = collections.deque([(0, 0, root)])
        while q:
            col, row, node = q.popleft()
            column_map[col].append((node.val, row))
            if node.left:
                q.append((col - 1, row+1, node.left))
            if node.right:
                q.append((col + 1, row+1, node.right))

        # print(column_map)
        res = []
        for col in sorted(column_map.keys()):
            vals = [i[0] for i in sorted(column_map[col], key = lambda x:(x[1], x[0]))]
            res.append(vals)
        
        return res

        
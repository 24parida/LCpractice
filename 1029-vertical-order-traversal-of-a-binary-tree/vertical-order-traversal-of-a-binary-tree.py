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
        min_col, max_col = float('inf'), float('-inf')
        while q:
            col, row, node = q.popleft()
            min_col = min(min_col, col)
            max_col = max(max_col, col)

            column_map[col].append((node.val, row))
            if node.left:
                q.append((col - 1, row+1, node.left))
            if node.right:
                q.append((col + 1, row+1, node.right))

        res = []
        for col in range(min_col, max_col+1):
            if col not in column_map:
                continue
            vals = [i[0] for i in sorted(column_map[col], key = lambda x:(x[1], x[0]))]
            res.append(vals)
        
        return res

        
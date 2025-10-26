"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        q = collections.deque([root])
        while q:
            N = len(q)
            for i in range(N):
                node = q.popleft()
                node.next = None if i == N-1 else q[0]
                
                if node.left and node.right:
                    q.append(node.left)
                    q.append(node.right)
        return root
        
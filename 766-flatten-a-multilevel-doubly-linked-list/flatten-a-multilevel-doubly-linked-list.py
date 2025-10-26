"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        dummy = Node(0)
        cur = dummy

        stack = [head]
        while stack:
            node = stack.pop()

            node.prev = cur
            cur.next = node
            cur = cur.next

            if node.next: stack.append(node.next)
            if node.child: 
                stack.append(node.child)
                node.child = None
        
        dummy.next.prev = None
        return dummy.next
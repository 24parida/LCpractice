# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2
        

        def recursivelyAdd(node1, node2, carryIn):
            node1Val = node1.val if node1 else 0
            node2Val = node2.val if node2 else 0

            if not node1 and not node2:
                if not carryIn:
                    return None
                return ListNode(carryIn, None)

            nodeSum = node1Val + node2Val + carryIn
            nodeVal = nodeSum % 10
            carryOut = nodeSum // 10

            node1Next, node2Next = node1.next if node1 else None, node2.next if node2 else None
            newNode = ListNode(nodeVal, recursivelyAdd(node1Next, node2Next, carryOut))
            return newNode
        
        return recursivelyAdd(l1, l2, 0)
            
            
                    
        
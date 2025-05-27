# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = ListNode()
        curr = root
        while any(lists):
            min_list = (0, float('inf'))
            for idx in range(len(lists)):
                if lists[idx] and lists[idx].val < min_list[1]:
                    min_list = (idx, lists[idx].val)
        
            curr.next = lists[min_list[0]]
            curr = curr.next

            lists[min_list[0]] = lists[min_list[0]].next
            if not lists[min_list[0]]:
                lists.pop(min_list[0])
        return root.next
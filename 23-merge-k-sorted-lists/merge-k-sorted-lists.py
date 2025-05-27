# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for idx in range(len(lists)):
            if lists[idx]:
                min_heap.append((lists[idx].val, idx, lists[idx]))
        
        heapq.heapify(min_heap)
        
        root = ListNode()
        curr = root
        while min_heap:
            top = heapq.heappop(min_heap)
            curr.next = top[-1]
            curr = curr.next

            if top[-1].next:
                heapq.heappush(min_heap, (top[-1].next.val, top[1], top[-1].next))
        
        return root.next
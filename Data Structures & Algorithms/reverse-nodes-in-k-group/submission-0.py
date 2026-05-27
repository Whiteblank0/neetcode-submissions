# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        dummy = ListNode(next=head)
        p0 = dummy
        
        while n >= k:
            n -= k
            prev = None
            curr = p0.next
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            nex = p0.next
            p0.next.next = curr
            p0.next = prev
            p0 = nex

        return dummy.next
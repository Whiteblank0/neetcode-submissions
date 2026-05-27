# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head2 = self.reverseList(head)

        if n == 1:
            head3 = head2.next
            head2.next = None
            return self.reverseList(head3)
        else:
            prev = None
            curr = head2
            while n > 1:
                prev = curr
                curr = curr.next
                n -= 1
            prev.next = curr.next
            return self.reverseList(head2)
            
            
            
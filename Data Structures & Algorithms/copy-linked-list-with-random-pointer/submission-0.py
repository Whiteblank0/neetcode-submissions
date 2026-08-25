"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        curr = dummy
        dic = {}
        original = head

        while original:
            curr.next = Node(original.val)
            curr = curr.next
            dic[original] = curr
            original = original.next
        
        original = head
        copy = dummy.next
        while original:
            if original.random:
                copy.random = dic[original.random]
            
            original = original.next
            copy = copy.next
        
        return dummy.next
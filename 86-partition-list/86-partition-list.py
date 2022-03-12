# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        front, back, h = ListNode(), ListNode(), head
        f, b = front, back
        
        while h:
            if h.val < x:
                f.next = ListNode(val=h.val)
                f = f.next
            else:
                b.next = ListNode(val=h.val)
                b = b.next
            h = h.next
            
        f.next = back.next
                
        return front.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        front, back = head, head
        
        for i in range(0, n):
            back = back.next
            
        if not back:
            return front.next
            
        while back:
            back = back.next
            prev = front
            front = front.next
                
        prev.next = front.next
        
        return head
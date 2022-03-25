# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        f = []
        
        while True:
            f.append(head.val)
            if head.next is None:
                break
            else:
                head = head.next
                
        return f == f[::-1]
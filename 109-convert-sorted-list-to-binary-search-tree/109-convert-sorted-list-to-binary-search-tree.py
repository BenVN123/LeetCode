# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None;
        
        mid = Solution.middle(head)
        root = TreeNode(mid.val)
        
        if head == mid:
            return root
        
        root.left = Solution.sortedListToBST(self,head=head)
        root.right = Solution.sortedListToBST(self,head=mid.next)

        return root
    
    def middle(head):
        fast = head
        slow = head   
        prev = head
        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if prev != None:
            prev.next = None
        
        return slow
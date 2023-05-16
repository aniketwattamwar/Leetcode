# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head, n):
        slow = fast  = head
 
        for i in range(0,n):
            print(fast.val)
            fast = fast.next
    
        if not fast:                                            
            return head.next
        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next = slow.next.next
        print(head)
        return head
    
sol = Solution()

n = 2
# sol.removeNthFromEnd(head,n)
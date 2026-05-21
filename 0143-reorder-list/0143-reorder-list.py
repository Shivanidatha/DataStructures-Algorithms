# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        def reverse(l):
            curr=l
            prev=None

            while curr:
                nextnode=curr.next
                curr.next=prev
                prev=curr
                curr=nextnode
            return prev

        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        second=slow.next
        slow.next=None
        revlist=reverse(second)
        
        l=head
        r=revlist

        while r:
            lnext=l.next
            rnext=r.next

            l.next=r
            r.next=lnext
            l=lnext
            r=rnext
        
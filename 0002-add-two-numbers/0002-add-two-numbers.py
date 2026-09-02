# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=0
        t=1
        while l1!= None:
            num1+=l1.val*t
            l1=l1.next
            t*=10
        num2=0
        k=1
        while l2!= None:
            num2+=l2.val*k
            l2=l2.next
            k*=10
        res=num1+num2
        head= ListNode(0)
        if res==0:
            return head
        l=head
        while res!=0:
            remainder=res%10
            l.next=ListNode(remainder)
            l=l.next
            res//=10
        return head.next


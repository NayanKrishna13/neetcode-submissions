# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node=ListNode()
        head=node
        c=0
        while(c or l1 or l2):
            if l1:
                node.val+=l1.val
                l1=l1.next
            if l2:
                node.val+=l2.val
                l2=l2.next
            if c:
                node.val+=c
            if node.val>=10:
                node.val-=10
                c=1
            else:
                c=0
            #print("node.val,c",node.val,c)
            if (c==0) and not l1 and not l2:
                break
            node.next=ListNode()
            node=node.next
        return head

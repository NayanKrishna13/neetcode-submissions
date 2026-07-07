# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        ele=ListNode()
        head=ele
        while(list1 or list2):
            val1=101 if not list1 else list1.val
            val2=101 if not list2 else list2.val
            if val1<val2:
                ele.val=val1
                list1=list1.next
            elif val1>val2:
                ele.val=val2
                list2=list2.next
            else:
                ele.val=val1
                ele.next=ListNode(val2)
                ele=ele.next
                list1,list2=list1.next,list2.next
            if list1 or list2:
                ele.next=ListNode()
            ele=ele.next
        return head



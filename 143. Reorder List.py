# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        top, ans = head, head
        l = []
        head = head.next

        while head:
            l.append(head.val)
            head = head.next

        while l:
            top.next = ListNode(l[-1])
            top = top.next
            l.pop(-1)
            if l:
                top.next = ListNode(l[0])
                top = top.next
                l.pop(0)

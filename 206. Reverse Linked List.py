# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = curr = ListNode(-1)
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l.reverse()

        for i in l:
            temp = ListNode(i)
            curr.next = temp
            curr = curr.next

        return ans.next

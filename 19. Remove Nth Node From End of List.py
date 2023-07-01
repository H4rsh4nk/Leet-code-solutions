# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = []
        root, pointer = head, head
        index = 0

        while head:
            if index > n:
                pointer = pointer.next
            l.append(head.val)
            head = head.next
            index += 1
        # print(pointer.val)

        if len(l) == 1:
            return None
        # last element
        if n == 1:
            pointer.next = None
            return root
        # first element
        if n == len(l):
            return root.next
        # mid element:
        pointer.next = pointer.next.next
        return root

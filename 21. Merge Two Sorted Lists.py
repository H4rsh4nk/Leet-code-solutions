# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while True:
            if list1:
                l.append(list1.val)
                list1 = list1.next

            if list2:
                l.append(list2.val)
                list2 = list2.next    

            if not list1 and not list2:
                break
        
        l.sort()
        curr = ans = ListNode(-1)
        for i in l:
            temp = ListNode(i)
            curr.next = temp
            curr = curr.next

        return ans.next
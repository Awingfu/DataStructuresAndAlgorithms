# https://leetcode.com/problems/odd-even-linked-list/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        o = odd
        even = ListNode()
        e = even
        
        curr = head
        index = 1
        while curr:
            if index % 2 == 1:
                print('adding ' + str(curr.val) + ' to odd')
                o.next = curr
                o = o.next
            else:
                print('adding ' + str(curr.val) + ' to even')
                e.next = curr
                e = e.next
            index += 1
            curr = curr.next
        e.next = None
        o.next = even.next
        return odd.next
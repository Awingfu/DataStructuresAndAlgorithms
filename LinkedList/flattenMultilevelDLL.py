# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/submissions/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def get_last(self, node):
        t = node
        while t and t.next:
            t = t.next
        return t
    
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            if curr.child:
                nxt = curr.next
                curr.next = curr.child
                curr.child.prev = curr
                last_child = self.get_last(curr.child)
                if nxt:
                    nxt.prev = last_child
                last_child.next = nxt
                curr.child = None
            curr = curr.next
            
        return head
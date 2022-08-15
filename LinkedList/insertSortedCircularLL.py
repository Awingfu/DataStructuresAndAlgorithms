#https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        newNode = Node(insertVal)
        if not head:
            newNode.next = newNode
            return newNode

        prev = head
        curr = head.next
        toInsert = False
        while True:
            # case 1: we found spot
            if prev.val <= insertVal and insertVal <= curr.val:
                break
            # else prev is last spot
            elif prev.val > curr.val:
                # insertVal has to go at the tail and is less than all elements 
                if prev.val <= insertVal or insertVal <= curr.val:
                    break
            prev, curr = curr, curr.next
            # if we've done a full cycle
            if prev == head:
                break
        
        # Either we found place to insert or we insert anywhere 
        prev.next = newNode
        newNode.next = curr            
        
        return head
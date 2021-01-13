# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # edge case 0 node:
        if not head:
            return head
        prev = None
        curr = head
        while curr.next:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        curr.next = prev
        return curr
    

# Test
end = ListNode(6)
head = None
for i in range(5):
    temp = ListNode(5-i, end)
    end = temp
    head = temp

iterate = head
while iterate != None:
    print(str(iterate.val) + " ")
    iterate = iterate.next
    
sol = Solution()
head = sol.reverseList(head)
      
iterate = head
while iterate != None:
    print(str(iterate.val) + " ")
    iterate = iterate.next


            
        
        
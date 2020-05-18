# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # start at head node
        # 1 ptr for prev (init as head), 1 for current (init as head), 1 for after (init as head.next)
        # Iterative:
        # gen case: 
        # current.next = prev, after.next = current
        # edge cases:
        # if after == Null, just do current.next = prev, and head = current
        # if prev == head, just do current.next = null, after.next = current
        
        # edge case 0 node:
        if head == None:
            return head
        
        # edge case 1 node
        if head.next == None:
            return head
        
        prev = head
        curr = head
        after = head.next
        
        #first run
        # ie: pc-> a -> 2 -> 3 -> 4
        if prev == head:
            curr = after # move curr forward
            after = curr.next # move after forward
            prev.next = None # set prev -> null
            curr.next = prev # set curr -> prev

        # ie: NULL <-p <- c, a -> 3 -> 4
        # gen case
        while(after != None):
            prev = curr # move prev forward
            # ie: NULL <- 0 <- pc, a -> 2 -> 3
            curr = after # move curr forward
            # ie: NULL <- 0 <- p, ca -> 2 -> 3
            after = curr.next # move after forward
            # ie: NULL <- 0 <- p, c -> a -> 3
            curr.next = prev # set curr -> prev
            # ie: NULL <- 0 <- p <- c, a -> 3
        
        # after == NULL
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


            
        
        
# Node class
# for singly linked list
class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def appendToEnd(self, val):
        new_node = Node(val)
        new_node.next = None

        if self.head == None:
            self.head = new_node
        else:
            track = self.head
            while (track.next != None):
                track = track.next
            track.next = new_node

    def printList(self):
        track = self.head
        while(track):
            print(track.data)
            track = track.next

    def reverseRecursively(self, curr, prev): 
          
        # If last node mark it head 
        if curr.next is None : 
            self.head = curr  
              
            # Update next to prev node 
            curr.next = prev 
            return 
          
        # Save curr.next node for recursive call 
        next = curr.next
        # And update next  
        curr.next = prev 
      
        self.reverseRecursively(next, curr)  

    def reverseIteratively(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 

    def reverse(self, kind="recursive"): 
        if self.head is None: 
            return 
        if kind == "recursive":
            self.reverseRecursively(self.head, None) 
        elif kind == "iterative":
            self.reverseIteratively()
        else:
            print("what kind?")
        

# Test
llist = LinkedList()
llist.appendToEnd(1)
llist.appendToEnd(2)
llist.appendToEnd(3)
llist.appendToEnd(4)
llist.appendToEnd(5)

llist.printList()
llist.reverse()
llist.printList()
llist.reverse("iterative")
llist.printList()
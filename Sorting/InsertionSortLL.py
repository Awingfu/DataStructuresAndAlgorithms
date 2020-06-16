# Does not work

class Node: 
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

class Array:
  def __init__(self, startingNode):
    self.head = startingNode
    self.tail = startingNode
    self.isSorted = False

  def append(self, node):
    curr = self.head
    while(curr.next != None):
      curr = curr.next
    curr.next = node
    node.prev = curr
    self.tail = node
    self.isSorted = False
  
  def swap(self, node1, node2):
    firstNodeNext = node1.next
    firstNodePrev = node1.prev

    node1.next = node2.next
    node1.prev = node2.prev

    node2.next = firstNodeNext
    node2.prev = firstNodePrev

    if self.head == node1:
      self.head == node2
    if self.tail == node1:
      self.tail = node2
    if self.head == node2:
      self.head = node1
    if self.tail == node2:
      self.tail = node1
  
  # insert node1 to before node2
  def insert(self, node1, node2):
    prev = node1.prev
    prev.next = node1.next
    node1.prev = node2.prev
    node1.next = node2
    node2.prev = node1

    if self.tail == node1:
      self.tail = node2
    if self.head == node2:
      self.head = node1
  
  def insertionSort(self):
    curr = self.head
    nextNode = curr.next

    if curr == None or nextNode == None:
      return
    
    while (curr != None):
      curr = nextNode
      nextNode = curr.next

      # curr is in correct place
      if curr.prev.value <= curr.value:
        continue
      
      prev = curr.prev
      print('hi')
      while(prev.prev != None and prev.value > curr.value):
        prev = prev.prev
      print('inserting ' + str(curr.value) + ' before ' + str(prev.value))
      self.insert(curr, prev)

    self.isSorted = True

  def print(self):
    curr = self.head
    while(curr != None):
      print(curr.value)
      curr = curr.next

testArray = Array(Node(0))
testArray.append(Node(3))
testArray.append(Node(1))

testArray.print()

testArray.insertionSort()
testArray.print()
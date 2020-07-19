class Heap: 
  def __init__(self, heapType = "min"):
    self.type = heapType
    self.heap = []
    self.size = 0

  def print(self):
    print(self.type + " Heap:")
    print(self.heap)

  def getParentIndex(self, index):
    return (index - 1)//2
  
  def getLeftChildIndex(self, index):
    return index*2 + 1

  def getRightChildIndex(self, index):
    return index*2 + 2

  def hasParent(self, index):
    return index != 0 and (index - 1)//2 >= 0

  def hasLeftChild(self, index):
    return index*2 + 1 < self.size

  def hasRightChild(self, index):
    return index*2 + 2 < self.size

  def swap(self, index1, index2):
    temp = self.heap[index1]
    self.heap[index1] = self.heap[index2]
    self.heap[index2] = temp

  def peek(self):
    if self.size > 0:
      return self.heap[0]
    return None
  
  def poll(self):
    # remove top element
    removedElement = self.heap.pop(0)
    self.size -= 1
    # take the last element and push it to top
    self.heap = self.heap[-1:] + self.heap[:-1]
    self.heapifyDown()
    print("removing " + str(removedElement))
    return removedElement

  def insert(self, key):
    self.heap.append(key)
    self.size += 1
    self.heapifyUp()

  def heapifyUp(self):
    index = self.size - 1
    if self.type == "min":
      while(self.hasParent(index) and self.heap[self.getParentIndex(index)] > self.heap[index]):
        self.swap(self.getParentIndex(index), index)
        index = self.getParentIndex(index)
    else: 
       while(self.hasParent(index) and self.heap[self.getParentIndex(index)] < self.heap[index]):
        self.swap(self.getParentIndex(index), index)
        index = self.getParentIndex(index)
  
  def heapifyDown(self):
    index = 0
    if self.type == "min":
      while(self.hasLeftChild(index)):
        smallerChildIndex = self.getLeftChildIndex(index)
        if (self.hasRightChild(index) and self.heap[self.getRightChildIndex(index)] < self.heap[self.getLeftChildIndex(index)]):
          smallerChildIndex = self.getRightChildIndex(index)

        if (self.heap[index] < self.heap[smallerChildIndex]):
          return 
        else: 
          self.swap(index, smallerChildIndex)
          index = smallerChildIndex
    else:
      while(self.hasLeftChild(index)):
        biggerChildIndex = self.getLeftChildIndex(index)
        if (self.hasRightChild(index) and self.heap[self.getRightChildIndex(index)] > self.heap[self.getLeftChildIndex(index)]):
          biggerChildIndex = self.getRightChildIndex(index)

        if (self.heap[index] > self.heap[biggerChildIndex]):
          return 
        else: 
          self.swap(index, biggerChildIndex)
          index = biggerChildIndex


#test
heap = Heap("min")
heap.insert(0)
heap.insert(5)
heap.insert(6)
heap.insert(7)
heap.insert(1)
heap.insert(2)
heap.insert(3)
heap.insert(4)
heap.insert(-1)
heap.print()
heap.poll()
heap.poll()
heap.poll()
heap.poll()
heap.poll()
heap.poll()
heap.poll()
heap.poll()
heap.poll()

heap = Heap("max")
heap.insert(0)
heap.insert(5)
heap.insert(6)
heap.insert(7)
heap.insert(1)
heap.insert(2)
heap.insert(3)
heap.insert(4)
heap.insert(-1)
heap.print()
heap.poll()
heap.poll()
heap.poll()
heap.poll()
heap.poll()
heap.poll()
heap.poll()
heap.poll()
heap.poll()

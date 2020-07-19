#binary insertion sort

# plan
# iterate through the array from start to end
# first index will be marked as sorted (keep an index to mark the last sorted index)
# as we iterate through unsorted part, Binary Search on sorted array from 0 to mark to find index where to insert
# insert 

# [ 5, 9, 7, 2]

def bis(arr):
   if not arr or len(arr)==1: 
       return arr
   
   for i in range(1,len(arr)):
       temp_value = arr[i]
       new_index = binarySearchForIndex(arr[:i],temp_value)
       swap(arr, i, new_index)
   
   
# Returns index for insertion
# halfway point of arr -> half_value
# if half_value == value -> insert before
# if value < half_value & value > half_value - 1 -> insert before half_value
# if value > half_value -> look right
# if value < half_value & value < half_value - 1 -> look left
def binarySearchForIndex(arr, value):
    if len(arr) == 0: 
      return 0
    if len(arr) == 1:
      if arr[0] > value:
        return 0
      else:
        return 1
    
    half_index = len(arr) // 2
    half_value = arr[half_index]
    if value == half_value:
      return half_index
    elif value < half_value and value > arr[half_index-1]:
      return half_index
    elif value > half_value: # look right
      return half_index + binarySearchForIndex(arr[half_index:], value)
    else: # look left
      return binarySearchForIndex(arr[:half_index], value)

# index 1 is the current element, and index2 is where it should go (less than index1)
def swap(arr, index1, index2):
    while (index1 > index2):
        temp = arr[index1]
        arr[index1] = arr[index1-1]
        arr[index1-1] = temp
        index1 -= 1
        
unsortedArr = [ 5, 9, 7, 2, 5, 5]
bis(unsortedArr)
print(unsortedArr)

unsortedArr = [5,1]
bis(unsortedArr)
print(unsortedArr)

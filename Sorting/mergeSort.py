def mergesort(arr):
  if arr == None or len(arr) == 1:
    return arr
  left = arr[:len(arr)//2]
  right = arr[len(arr)//2:]
  return merge(mergesort(left), mergesort(right))

def merge(left, right):
  if left == None:
    return right
  if right == None: 
    return left
  result = []
  while len(left) > 0 and len(right) > 0:
    l = left[0]
    r = right[0]
    if l < r:
      result.append(left.pop(0))
    elif l >= r:
      result.append(right.pop(0))
  return result + left + right

arr = [1,5,2,6,4,3]
arr = mergesort(arr)
print(arr)
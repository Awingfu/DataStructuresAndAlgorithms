#https://leetcode.com/discuss/interview-question/861453/
def numberOfItems(s, start, end): # O(n*m) n is length of s, and m is length of indexes (start or end); space constant
  if len(start) != len(end):
    return 0

  result = []
  for i in range(len(start)):
    startIndex = start[i] - 1
    endIndex = end[i] - 1
    substring = s[startIndex:endIndex + 1] # inclusive

    compartmented = False
    validInputs = 0
    temp = 0
    for item in substring:
      if item == '|':
        if compartmented:
          validInputs += temp
        else:
          compartmented = True
        temp = 0
      if compartmented and item == '*':
        temp += 1
    result.append(validInputs)
  return result


print(numberOfItems('|**|*|*', [1,1], [5,6]) == [2,3])
print(numberOfItems('*|*|', [1], [3]) == [0])
print(numberOfItems('*|*|*|', [1], [6]) == [2])
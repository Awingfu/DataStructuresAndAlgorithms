def numberOfItems(s, start, end):
  if len(start) != len(end):
    return 0
  result = []
  for i in range(len(start)):
    startIndex = start[i] - 1
    endIndex = end[i] - 1
    substring = s[startIndex:endIndex + 1] # inclusive
    print(substring)
    compartmented = False
    finalized_count = 0
    temp = 0
    for item in substring:
      if item == '|':
        compartmented = not compartmented
        if compartmented == False:
          finalized_count += temp
          temp = 0
          compartmented = True
      if compartmented and item == '*':
        temp += 1
    result.append(finalized_count)
  print(result)
  return result


print(numberOfItems('|**|*|*', [1,1], [5,6]) == [2,3])
print(numberOfItems('*|*|', [1], [3]) == [0])
print(numberOfItems('*|*|*|', [1], [6]) == [2])
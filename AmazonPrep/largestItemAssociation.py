# doesnt combine items if they are part of a set
def largestItemAssociation(itemAssociation):
  groupDict = {}
  nextGroupStart = 0
  for pair in itemAssociation: # n^2 total
    first = pair[0]
    second = pair[1]
    added = False
    for groupIndex in range(nextGroupStart): # n
      if first in groupDict[groupIndex] or second in groupDict[groupIndex]:
        groupDict[groupIndex].add(first)
        groupDict[groupIndex].add(second)
        added = True
    if added == False: # make a new group
      groupDict[nextGroupStart] = set([first,second])
      nextGroupStart += 1
  # print(groupDict)

  largestGroup = []
  maxSize = 0
  for groupIndex in range(nextGroupStart): # n^2 log n
    currentGroup = list(groupDict[groupIndex])
    currentGroup.sort() # nlogn
    currentGroupSize = len(currentGroup)
    if currentGroupSize > maxSize:
      maxSize = currentGroupSize
      largestGroup = currentGroup
    elif currentGroupSize == maxSize: # for the lexographic order
      # currentGroup has values less than largest group
      if "".join(largestGroup) > "".join(currentGroup): 
        largestGroup = currentGroup

  return largestGroup

print(largestItemAssociation([['item1', 'item2'], ['item3', 'item4'], ['item4', 'item5']]))
print(largestItemAssociation([['item1', 'item2'], ['item4', 'item5'], ['item3', 'item4'], ["item1","item4"]]))
print(largestItemAssociation([['item1', 'item2'], ['item4', 'item5'], ['item3', 'item4'], ["item1","item4"],['item7', 'item8'], ['item10', 'item11'], ['item9', 'item10'], ["item7","item10"],])) # 0 is less than i
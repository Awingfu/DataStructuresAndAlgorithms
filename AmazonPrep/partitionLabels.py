# https://leetcode.com/problems/partition-labels/

def partitionLabels(s):
  # loop through s
  # store letter: index in dict
  # where index will become the index it was last seen

  # set result = []
  # set maxIndex = 0
  # set currentLen = 0
  # loop through s by index
  # for each index, 
  # maxIndex = max(current letter's max index, maxIndex)
  # if letter's last index is now and maxIndex is now
  # currentLen into result
  # currentLen = 0
  lastSeen = {}
  for i in range(len(s)):
    lastSeen[s[i]] = i
  
  result = []
  maxIndex = 0
  currentLen = 0
  for i in range(len(s)):
    currentLen += 1
    letter = s[i]
    maxIndex = max(maxIndex,lastSeen[letter])
    if maxIndex == i:
      result.append(currentLen)
      currentLen = 0

  # print(result)
  return result

test = partitionLabels("ababcbacadefegdehijhklij")
print(test == [9,7,8])
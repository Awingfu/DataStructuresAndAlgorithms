# https://leetcode.com/discuss/interview-question/874984/
def findMinComplexity(complexities, days):
  numJobs = len(complexities)
  # base cases
  if numJobs < days:
    return -1
  if numJobs == days:
    return sum(complexities)
  if days == 1:
    return max(complexities)

  resultGrid =[[0 for i in range(days+1)] for j in range(numJobs + 1)]

  # case where only 1 day given different complexities
  maxComplexity = 0
  for i in range(1,numJobs+1):
    maxComplexity = max(maxComplexity, complexities[i-1])
    resultGrid[i][1] = maxComplexity
  
  for j in range(2,days+1): # for days 2 to last
    for i in range(j,numJobs+1): # for jobs from 2 to last because you jobs >= days
      maxComplexity = 0
      minValue = float("inf")
      # for row in reversed(range(j, i+1)):
      #   maxComplexity = max(complexities[row-1], maxComplexity)
      #   minValue = min(minValue,maxComplexity + resultGrid[row-1][j-1])
      
    resultGrid[i][j] = minValue
    print(resultGrid)
  return resultGrid
  # return resultGrid[numJobs][days]

# findMinComplexity([30,10,40,20,50],2)
result = findMinComplexity([30,10,40,20,50],4)
print(result)
for row in result:
  print(row)
# print(findMinComplexity([30,10,40,20,50],3))
# test2 = findMinComplexity([9,9,9], 4)
# print(test2) # -1
# test3 = findMinComplexity([1,1,1], 3)
# print(test3) # 3
# test4 = findMinComplexity([7,1,7,1,7,1], 3)
# print(test4) # 15
# test5 = findMinComplexity([11,111,22,222,33,333,44,444], 6)
# print(test5) # 843
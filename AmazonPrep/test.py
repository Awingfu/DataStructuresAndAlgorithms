# https://leetcode.com/discuss/interview-question/874984/
def minDifficulty(jobDifficulty, d):
    """
    :type jobDifficulty: List[int]
    :type d: int
    :rtype: int
    """
    return minDiff(jobDifficulty, 0, d)

  
def minDiff(jobs, i, d):
  numJobs = len(jobs)
  if i == numJobs and d ==0:
    return 0
  if d == 0:
    return float('inf')

  currMax = float('-inf')
  minVal = float('inf')
  for j in range(i, numJobs):
    currMax = max(currMax, jobs[j])
    minVal = min(minVal, currMax + minDiff(jobs, j+1, d-1))

  return minVal
# minDifficulty([30,10,40,20,50],2)
# result = minDifficulty([30,10,40,20,50],4)
# print(result)
# for row in result:
#   print(row)
# print(minDifficulty([30,10,40,20,50],3))
# test2 = minDifficulty([9,9,9], 4)
# print(test2) # -1
# test3 = minDifficulty([1,1,1], 3)
# print(test3) # 3
test4 = minDifficulty([7,1,7,1,7,1], 3)
print(test4) # 15
# test5 = minDifficulty([11,111,22,222,33,333,44,444], 6)
# print(test5) # 843
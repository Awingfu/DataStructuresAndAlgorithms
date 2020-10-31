# https://leetcode.com/discuss/interview-question/874984/
def minDifficulty(jobDifficulty, d):
    """
    :type jobDifficulty: List[int]
    :type d: int
    :rtype: int
    """
    numJobs = len(jobDifficulty)
    if jobDifficulty == None:
        return 0
    if numJobs < d:
        return -1
    if numJobs == d:
        return sum(jobDifficulty)
    if d == 1:
        return max(jobDifficulty)
    
    dpTable = [[float("inf") for _ in range(numJobs + 1)] for _ in range(d+1)]
    dpTable[0][0] = 0
    print(dpTable)
    
    for i in range(1, d+1):
        # starts at i, bc there must be at least i days
        # ends at numJobs - d + i + 1 to save enough jobs for other days
        for j in range(i, numJobs-d+i+1): 
            for k in range(i-1, j):
                print("with only ",i, " day")
                print("with jobs ", jobDifficulty[:j])
                print("k = ", k)
                dpTable[i][j] = min(dpTable[i][j], 
                  dpTable[i-1][k] + maxWork(jobDifficulty, k+1, j))
                print(dpTable[i][j])
    for row in dpTable:
      print(row)
    return dpTable[d][numJobs]

def maxWork(jobDifficulty, fromJob, toJob):
    maximum = 0
    for i in range(fromJob-1, toJob):
        maximum = max(maximum, jobDifficulty[i])
    return maximum

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
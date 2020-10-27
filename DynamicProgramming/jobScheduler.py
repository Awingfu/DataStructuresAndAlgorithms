# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
class Solution:
    # def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
    #       jd = jobDifficulty
    #       L = len(jd)
    #       if d > L:
    #           return -1
          
    #       def dp(index, days):
              
    #           if index >= L:
    #               if days == 0:
    #                   return 0
    #               else:
    #                   return float("inf")
    #           if days <= 0:
    #               return float("inf")
              
    #           ret = float("inf")
    #           curmax = -1
    #           for i in range(index, L):
    #               curmax = max(curmax, jd[i])
    #               ret = min(ret, curmax + dp(i+1, days-1))
    #           # print(index, days, ret)
    #           return ret
          
    #       return dp(0, d)
    
    def minDifficulty(self, jobDifficulty, d: int) -> int:
        length = len(jobDifficulty)
        if d > length: # no way to schedule jobs
            return -1
        
        dp = [float("inf")] * (length + 1)
        print(dp)
        dp[-1] = 0
        print(dp)
        for _ in range(d): # for each day
            dp2 = [float("inf")] * (length + 1)
            for i in range(length): #for each job dif index
                curmax = -1
                for j in range(i, length): #start at i
                    curmax = max(curmax, jobDifficulty[j]) 
                    print(j, curmax)
                    dp2[i] = min(dp2[i], curmax + dp[j+1])
                    print(dp2)
            dp = dp2
            
        return dp[0]

test = Solution()
test1 = test.minDifficulty([6,5,4,3,2,1], 2)
print(test1) # 7
# test2 = test.minDifficulty([9,9,9], 4)
# print(test2) # -1
# test3 = test.minDifficulty([1,1,1], 3)
# print(test3) # 3
# test4 = test.minDifficulty([7,1,7,1,7,1], 3)
# print(test4) # 15
# test5 = test.minDifficulty([11,111,22,222,33,333,44,444], 6)
# print(test5) # 843
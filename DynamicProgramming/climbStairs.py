# https://leetcode.com/problems/climbing-stairs/submissions/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        last2Steps = [1,2]
        
        for i in range(3, n+1):
            nextStep = last2Steps[0] + last2Steps[1]
            last2Steps[0] = last2Steps[1]
            last2Steps[1] = nextStep
            
        return last2Steps[1]
        # mem = {}
        # mem[0] = 0
        # mem[1] = 1
        # mem[2] = 2
        # for i in range(3, n+1):
        #     # there's only 1 way to get here from each 1 back and 2 back
        #     mem[i] = mem[i-1] + mem[i-2]
        # return mem[n]
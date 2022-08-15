# https://leetcode.com/problems/n-th-tribonacci-number/submissions/

class Solution:
    def tribonacci(self, n: int) -> int:
        mem = [0,1,1]
        if n < len(mem):
            return mem[n]
        
        for i in range(3, n+1):
            new = sum(mem)
            mem[0] = mem[1]
            mem[1] = mem[2]
            mem[2] = new
            
        return mem[-1]
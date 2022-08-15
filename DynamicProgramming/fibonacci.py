#https://leetcode.com/problems/fibonacci-number/submissions/

class Solution:
    def fib(self, n: int) -> int:
        mem = [0,1]
        if n < 2:
            return mem[n]
        for i in range(2,n+1):
            new = sum(mem)
            mem[0] = mem[1]
            mem[1] = new
        return mem[-1]
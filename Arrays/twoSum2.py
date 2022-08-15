# https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1153/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r] 
            if total == target:
                return [l+1,r+1]
            elif total < target:
                l += 1
            else:
                r -= 1
        
        
        # should never hit
        return [1,1]
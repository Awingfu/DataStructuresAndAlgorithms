# https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1154/
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sumation = 0
        for idx, num in enumerate(nums):
            if idx % 2 == 0:
                sumation += num
        return sumation
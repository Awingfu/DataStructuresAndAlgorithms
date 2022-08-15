# https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1299/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window with ptrs
        # keep minLength
        # left and right start at 0
        # move right until sum >= target. update minLength as min(minL, r-l)
        # move left until sum < target, but if sum now equals target, update minL
        minL = len(nums) + 1
        l = 0
        r = 0
        rollingSum = 0
        while r < len(nums):
            rollingSum += nums[r]
            while rollingSum >= target and l <= r:
                minL = min(minL, r-l+1)
                rollingSum -= nums[l]
                l += 1
            r += 1
            
        if minL == len(nums) + 1:
            return 0
        return minL
            
                
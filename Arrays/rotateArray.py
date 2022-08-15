# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]


#     def rotate(self, nums: List[int], k: int) -> None:
#         n = len(nums)
#         k %= n

#         self.reverse(nums, 0, n - 1)
#         self.reverse(nums, 0, k - 1)
#         self.reverse(nums, k, n - 1)
    
#     def reverse(self, nums: list, start: int, end: int) -> None:
#         while start < end:
#             nums[start], nums[end] = nums[end], nums[start]
#             start, end = start + 1, end - 1
       
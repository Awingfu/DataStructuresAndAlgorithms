# https://leetcode.com/problems/container-with-most-water/
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # brute force
        # max = 0
        # for each bar i from 0 to len - 1
        # for each bar after, j, from i+1 to len
        # max = max(min(i,j) * (j-i),max)
        # max_volume = 0
        # for i in range(len(height)-1):
        #     for j in range(i+1,len(height)):
        #         height_i = height[i]
        #         height_j = height[j]
        #         max_volume = max(min(height_i,height_j) * (j-i), max_volume)
        # return max_volume
        
        # two pointer method
        max_volume = 0
        start = 0
        end = len(height)-1
        while start < end:
            left_h = height[start]
            right_h = height[end]
            curr_volume = min(left_h,right_h) * (end-start)
            max_volume = max(max_volume,curr_volume)
            if left_h > right_h:
                end -= 1
            else:
                start += 1
        return max_volume
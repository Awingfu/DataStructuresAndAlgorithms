class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # o(n^2) DOESNT WORK
        # base cases: if height length < 2, return 0
        # loop through height
        # if found number > 0, store it in current_height and store current_index
        # start second loop to end of array
        # store sum of next values into already_fill
        # until you find value equally as high or higher
        # if you do, take current_height * (index - current-index) - already_fill and add to output, start first loop at most recent index
        # if not, do nothing and continue first loop
        # if height is None or len(height) < 2:
        #     return 0
        
        # output = 0
        # i = 0
        # while i < len(height):
        #     j = i+1
        #     already_fill = 0
        #     lowest_point = height[i]
        #     while j < len(height):
        #         # print(i,j)
        #         if height[j] > height[i] or (j == len(height) - 1 and lowest_point < min(height[i],height[j])):
        #             output += min(height[i],height[j]) * (j - i - 1) - already_fill
        #             already_fill = 0
        #             i = j - 1 # to stop double counting and account for i+=1
        #             break
        #         else: 
        #             already_fill += height[j]
        #             if height[j] < lowest_point:
        #                 lowest_point = height[j]
        #         j += 1
        #     i += 1
        # return output
        
        # O(N) time O(1) space
        left_ind = 0
        right_ind = len(height) - 1
        max_height_left = 0
        max_height_right = 0
        water = 0
        while left_ind < right_ind:
          if height[left_ind] < height[right_ind]:
            if height[left_ind] > max_height_left:
              max_height_left = height[left_ind]
            else:
              water += max_height_left - height[left_ind]
            left_ind += 1
          else:
            if height[right_ind] > max_height_right:
              max_height_right = height[right_ind]
            else:
              water += max_height_right - height[right_ind]
            right_ind -= 1
        return water
            
test = Solution()

height1 = [4,2,0,3,2,5]
height2 = [0,1,0,2,1,0,1,3,2,1,2,1]
height3 = [0,1,0,2,1,0,1,3]
height4 = [3,2,1,2,1]
height5 = [4,2,3]
print(test.trap(height1)) # 9
print(test.trap(height2)) # 6
print(test.trap(height3)) # 5
print(test.trap(height4)) # 1
print(test.trap(height5)) # 1

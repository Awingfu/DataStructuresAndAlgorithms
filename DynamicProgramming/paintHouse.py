# https://leetcode.com/problems/paint-house/submissions/

class Solution:
#     def minCost(self, costs: List[List[int]]) -> int:
#         cache = [[0 for x in range(len(costs[0]))] for x in range(len(costs))]
#         for house_idx, house_costs in enumerate(costs):
#             for color_idx, color_cost in enumerate(house_costs):
#                 if house_idx == 0:
#                     cache[house_idx][color_idx] = color_cost
#                     continue
#                 previousHouseCosts = cache[house_idx - 1][0:color_idx] + cache[house_idx - 1][color_idx+1:]
#                 cache[house_idx][color_idx] = color_cost + min(previousHouseCosts)
            
#         return min(cache[-1])
    
    def minCost(self, costs: List[List[int]]) -> int:
        dp = costs[0]
        
        for house_num in range(1,len(costs)):
            color_costs = costs[house_num]
            new_dp = []
            for color_idx, cost in enumerate(color_costs):
                bestCost = cost + min(dp[:color_idx] + dp[color_idx+1:])
                new_dp.append(bestCost)
            dp = new_dp
        return min(dp)
                
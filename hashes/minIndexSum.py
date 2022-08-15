# https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1177/
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # iterate through first list with hashmap: key is name, val is [index]
        # iterate through second list, if item in hashmap, append to value with index
        # iterate through hashmap keys, only if val is len 2, calc sum, and keep track of least
        # return least
        common = collections.defaultdict(list)
        for idx, val in enumerate(list1):
            common[val].append(idx)
            
        for idx, val in enumerate(list2):
            common[val].append(idx)
            
        
        # find min index sum
        minIndexSum = len(list1) + len(list2)
        for key in common:
            if len(common[key]) == 2:
                minIndexSum = min(sum(common[key]), minIndexSum)
        
        result = []
        for key in common:
            if len(common[key]) == 2 and sum(common[key]) == minIndexSum:
                result.append(key)
                
        return result
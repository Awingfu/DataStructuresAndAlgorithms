# https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1170/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        
        while len(result) < numRows:
            if len(result) == 0:
                result.append([1])
                continue   
            newRow = []
            prevRow = result[-1]
            prevValue = 0
            for idx in range(len(prevRow)):
                newRow.append(prevValue + prevRow[idx])
                prevValue = prevRow[idx]
            newRow.append(1)
            result.append(newRow)
            
        return result
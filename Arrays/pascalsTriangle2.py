# https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1171/
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prevRow = [1]
        
        for _ in range(rowIndex): 
            newRow = []
            prevValue = 0
            for idx in range(len(prevRow)):
                newRow.append(prevValue + prevRow[idx])
                prevValue = prevRow[idx]
            newRow.append(1)
            prevRow = newRow
            
        return prevRow
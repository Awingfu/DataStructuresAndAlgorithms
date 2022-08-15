# https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1117/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # loop through both at the same time
        # map char in s to char in t
        # if char from s in map, doesnt match char in t, return false
        
        letterMap = {}
        lettersUsed = set()
        for i in range(len(s)):
            if s[i] in letterMap:
                if letterMap[s[i]] != t[i]:
                    return False
            else:
                if t[i] in lettersUsed:
                    return False
                letterMap[s[i]] = t[i]
                lettersUsed.add(t[i])
                
        return True
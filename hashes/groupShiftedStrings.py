# https://leetcode.com/problems/group-shifted-strings/
class Solution:
    def shiftLetter(self, l, shift):
        return chr((ord(l) - shift) % 26 + ord('a'))
       
    # move first letter to a
    def getHashKey(self, s):
        # determine shift
        shift = ord(s[0])
        
        hashKey = ''
        for letter in s:
            hashKey += self.shiftLetter(letter, shift)
        return hashKey 
    
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for string in strings:
            key = self.getHashKey(string)
            groups[key].append(string)
        
        return list(groups.values())
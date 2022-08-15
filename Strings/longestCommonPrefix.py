# https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1162/

# i could also have just scanned once, keeping track of prefix and keep comparing against next val
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # find smallest word
        # create set of each prefix possibility
        # iterate through list, check if prefix is valid, if not, remove
        # return largest prefix left or ''
        if not strs:
            return ''
        smallest = strs[0]
        smallestSize = len(strs[0]) 
        for word in strs:
            if len(word) < smallestSize:
                smallestSize = len(word)
                smallest = word
        
        possiblePrefixes = set()
        currentPrefix = ''
        for letter in smallest:
            currentPrefix += letter
            possiblePrefixes.add(currentPrefix)
            
        for word in strs:
            prefixesToRemove = []
            for prefix in possiblePrefixes:
                if len(prefix) > len(word):
                    prefixesToRemove.append(prefix)
                elif prefix != word[0:len(prefix)]:
                    prefixesToRemove.append(prefix)
            for prefix in prefixesToRemove:
                possiblePrefixes.remove(prefix)
        
        longestPrefix = ''
        longestSize = 0
        for prefix in possiblePrefixes:
            if len(prefix) > longestSize:
                longestSize = len(prefix)
                longestPrefix = prefix
        return longestPrefix
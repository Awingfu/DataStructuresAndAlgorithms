# https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1161/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or needle == '':
            return 0
        needle_start = needle[0]
        
        for idx, val in enumerate(haystack):
            if val == needle_start:
                if len(haystack)- idx < len(needle):
                    return -1
                elif needle == haystack[idx:idx + len(needle)]:
                    return idx
        return -1
                    
#https://leetcode.com/problems/roman-to-integer/
conversion = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1
}
exceptions = set(["CM","CD","XC","XL","IX","IV"])
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        i = 0
        while i < len(s):
            letter = s[i]
            if i == len(s) - 1:
                result += conversion[letter]
                break
            else:
                next_letter = s[i+1]
                if letter + next_letter in exceptions:
                    result += conversion[letter + next_letter]
                    i += 1
                else:
                    result += conversion[letter]
                i += 1
        return result
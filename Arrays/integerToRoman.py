# 
# https://leetcode.com/problems/integer-to-roman/

digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), 
          (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = []
        for (value,letter) in digits:
            if num == 0:
                break
            count = num // value
            num = num % value
            result.append(letter * count)
        return "".join(result)
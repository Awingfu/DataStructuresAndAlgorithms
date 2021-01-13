# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        results = self.phoneNumberLetters(digits[0])
        for digit in digits[1:]:
            letters = self.phoneNumberLetters(digit)
            new_results = []
            for combo in results:
                for letter in letters:
                    new_results.append(combo+letter)
            results = new_results
        return results
            
        
    def phoneNumberLetters(self, num):
        phoneNumbers = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        return phoneNumbers[num]
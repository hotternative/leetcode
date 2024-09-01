# 41 ms Beats 83.49%

class Solution:
    def romanToInt(self, s: str) -> int:

        conversion_dict_combined = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        conversion_dict_single_digit = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        p = 0
        sum = 0
        while p < len(s):

            if s[p:p + 2] in conversion_dict_combined:
                sum += conversion_dict_combined[s[p:p + 2]]
                p += 2
            else:
                sum += conversion_dict_single_digit[s[p]]
                p += 1

        return sum

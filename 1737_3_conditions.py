# Created on 04/02/2021
import string

class Solution:

    @staticmethod
    def _condition1(a, b):
        m1 = 1000000
        for s in string.ascii_lowercase[:-1]:
            counta = 0
            for c in a:
                if c > s:
                    counta += 1

            countb = 0
            for c in b:
                if c <= s:
                    countb += 1
            if m1 > (counta + countb):
                m1 = counta + countb
        return m1

    @staticmethod
    def _condition2(a, b):
        m2 = 1000000
        for s in string.ascii_lowercase[:-1]:
            countb = 0
            for c in b:
                if c > s:
                    countb += 1

            counta = 0
            for c in a:
                if c <= s:
                    counta += 1

            if m2 > (counta + countb):
                m2 = counta + countb
        return m2

    @staticmethod
    def _condition3(a, b):
        # condition 3:
        m3 = 1000000
        for s in string.ascii_lowercase:
            counta = 0
            for c in a:
                if c != s:
                    counta += 1
            countb = 0
            for c in b:
                if c != s:
                    countb += 1
            if m3 > (counta+countb):
                m3 = counta + countb
        return m3


    def minCharacters(self, a: str, b: str) -> int:
        # condition 1:
        m1 = self._condition1(a, b)

        # condition 2:
        m2 = self._condition2(a, b)


        m3 = self._condition3(a, b)

        return min([m1, m2, m3])

a = "aba"; b = "caa"
print(Solution.minCharacters(Solution, a, b))

a = "dabadd";b = "cda"
print(Solution.minCharacters(Solution, a, b))
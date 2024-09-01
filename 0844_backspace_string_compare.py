class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def find_final(s):
            i, s_final = 0, ''
            for c in s:
                if c != '#':
                    s_final += c
                else:
                    s_final = s_final[:-1]
            print(s_final)
            return s_final

        return find_final(s) == find_final(t)
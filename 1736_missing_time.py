# Created on 04/02/2021
class Solution:

    def maximumTime(self, time: str) -> str:
        l = list(time)
        for i, c in enumerate(l):
            if c == '?':
                if i == 0:
                    if l[1] == '?' or int(l[1]) < 4:
                        l[i] = '2'
                    else:
                        l[i] = '1'

                elif i == 1:
                    if l[0] == '2':
                        l[i] = '3'
                    else:
                        l[i] = '9'
                elif i == 3:
                    l[i] = '5'
                elif i == 4:
                    l[i] = '9'


        return "".join(l)

i = Solution.maximumTime(Solution, '?1:11')
print(i)

i = Solution.maximumTime(Solution, '1?:11')
print(i)

i = Solution.maximumTime(Solution, '11:?1')
print(i)

i = Solution.maximumTime(Solution, "2?:?0")
print(i)


i = Solution.maximumTime(Solution, "?4:03")
print(i)
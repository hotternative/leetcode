from copy import copy

class Solution:
    def reinitializePermutation(self, n: int):
        original_perm = list(range(n))
        perm = list(range(n))
        cnt = 0
        arr = [None] * n
        print(original_perm)
        while arr != original_perm:
            arr = [None] * n

            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm[int(i / 2)]
                else:
                    arr[i] = perm[int(n / 2 + (i - 1) / 2)]

            perm = arr
            print(perm)
            cnt += 1

        return cnt

ans  = Solution.reinitializePermutation(Solution, 2)
print(ans)

ans  = Solution.reinitializePermutation(Solution, 4)
print(ans)


ans  = Solution.reinitializePermutation(Solution, 6)
print(ans)

ans  = Solution.reinitializePermutation(Solution, 8)
print(ans)

ans  = Solution.reinitializePermutation(Solution, 10)
print(ans)

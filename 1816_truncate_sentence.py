class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        w = s.split(" ")
        return " ".join(w[:k])

a = Solution.truncateSentence(Solution, "Hello how are you Contestant", 4)
print(a)


s = "What is the solution to this problem"
k = 4

a = Solution.truncateSentence(Solution, s, k)
print(a)

s = "chopper is not"
k = 5
a = Solution.truncateSentence(Solution, s, 5)
print(a)

class Solution:
    def totalMoney(self, n: int) -> int:
        # 1 week will have 1 +...+ 7 = 28
        # K whole weeks will have 28 + 35 + ...
        # the remainder m days will have (1 + K) + (2 + K) + ...

        number_of_weeks = n // 7
        ans = 0
        for week in range(number_of_weeks):
            ans += 28 + week * 7

        number_of_extra_days = n % 7
        for day in range(number_of_extra_days):
            ans += day + number_of_weeks + 1

        return ans



from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_factor = max((f for f, _ in items), default=0)

        freq = [0] * (max_factor + 1)
        for factor, _ in items:
            freq[factor] += 1

        multiples = [0] * (max_factor + 1)
        for d in range(1, max_factor + 1):
            total = 0
            for m in range(d, max_factor + 1, d):
                total += freq[m]
            multiples[d] = total

        dp = [0] * (budget + 1)

        for factor, price in items:
            if price > budget:
                continue
            first_copy_gain = multiples[factor]
            for b in range(budget, price - 1, -1):
                candidate = dp[b - price] + first_copy_gain
                if candidate > dp[b]:
                    dp[b] = candidate

        for _, price in items:
            if price > budget:
                continue
            for b in range(price, budget + 1):
                candidate = dp[b - price] + 1
                if candidate > dp[b]:
                    dp[b] = candidate

        return max(dp)
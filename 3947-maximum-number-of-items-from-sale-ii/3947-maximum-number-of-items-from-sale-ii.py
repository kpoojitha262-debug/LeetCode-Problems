class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_f = max(f for f, _ in items)
        factor_count = [0] * (max_f + 1)
        min_price = items[0][1]
        for f, p in items:
            factor_count[f] += 1
            if p < min_price:
                min_price = p

        multiples_count = [0] * (max_f + 1)
        for f in range(1, max_f + 1):
            if factor_count[f] > 0:
                for m in range(f, max_f + 1, f):
                    multiples_count[f] += factor_count[m]

        pairs = []
        for f, p in items:
            gain = multiples_count[f] - 1
            if gain > 0:
                pairs.append((p, gain))

        pairs.sort()
        total = 0
        rem = budget
        for p, gain in pairs:
            if rem < p or p >= 2 * min_price:
                break
            take = min(gain, rem // p)
            total += take * 2
            rem -= take * p

        total += rem // min_price
        return total
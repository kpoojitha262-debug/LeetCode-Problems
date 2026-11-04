import heapq
import collections
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        costs = [0] * n
        
        low = []
        high = []
        sum_low = 0
        sum_high = 0
        count_low = 0
        count_high = 0
        lazy = collections.defaultdict(int)
        
        def balance():
            nonlocal sum_low, sum_high, count_low, count_high
            
            while low and lazy[-low[0]] > 0:
                lazy[-heapq.heappop(low)] -= 1
            while high and lazy[high[0]] > 0:
                lazy[heapq.heappop(high)] -= 1
                
            while count_low > count_high + 1:
                val = -heapq.heappop(low)
                sum_low -= val
                count_low -= 1
                heapq.heappush(high, val)
                sum_high += val
                count_high += 1
                while low and lazy[-low[0]] > 0:
                    lazy[-heapq.heappop(low)] -= 1

            while count_low < count_high:
                val = heapq.heappop(high)
                sum_high -= val
                count_high -= 1
                heapq.heappush(low, -val)
                sum_low += val
                count_low += 1
                while high and lazy[high[0]] > 0:
                    lazy[heapq.heappop(high)] -= 1
        
        for i in range(n):
            if not low or nums[i] <= -low[0]:
                heapq.heappush(low, -nums[i])
                sum_low += nums[i]
                count_low += 1
            else:
                heapq.heappush(high, nums[i])
                sum_high += nums[i]
                count_high += 1
            
            if i >= x:
                rem = nums[i - x]
                lazy[rem] += 1
                if low and rem <= -low[0]:
                    sum_low -= rem
                    count_low -= 1
                else:
                    sum_high -= rem
                    count_high -= 1
                    
            balance()
            
            if i >= x - 1:
                median = -low[0]
                cost = (median * count_low - sum_low) + (sum_high - median * count_high)
                costs[i] = cost

        dp = [[float('inf')] * (k + 1) for _ in range(n)]
        
        for i in range(n):
            dp[i][0] = 0
            
        for i in range(x - 1, n):
            for j in range(1, k + 1):
                skip = dp[i - 1][j] if i > 0 else float('inf')
                
                if i - x >= 0:
                    take = costs[i] + dp[i - x][j - 1]
                else:
                    take = costs[i] if j == 1 else float('inf')
                
                dp[i][j] = min(skip, take)
                
        return dp[-1][k]
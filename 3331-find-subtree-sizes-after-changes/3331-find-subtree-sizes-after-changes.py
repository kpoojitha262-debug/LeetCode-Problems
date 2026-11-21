from collections import defaultdict
from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = defaultdict(list)
        for i in range(1, n):
            adj[parent[i]].append(i)

        new_parent = parent[:]
        last_seen = {}

        def find_ancestors(node: int) -> None:
            char = s[node]
            prev = last_seen.get(char)
            if prev is not None and prev != node:
                new_parent[node] = prev

            old_val = last_seen.get(char)
            last_seen[char] = node

            for child in adj[node]:
                find_ancestors(child)

            if old_val is not None:
                last_seen[char] = old_val
            else:
                del last_seen[char]

        find_ancestors(0)

        new_adj = defaultdict(list)
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)

        ans = [0] * n

        def calc_size(node: int) -> int:
            total = 1
            for child in new_adj[node]:
                total += calc_size(child)
            ans[node] = total
            return total

        calc_size(0)
        return ans
class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        import bisect


class Solution:

    def findTheDistanceValue(
        self, arr1: list[int], arr2: list[int], d: int
    ) -> int:
        arr2.sort()
        count = 0

        for x in arr1:
            idx = bisect.bisect_left(arr2, x)
            has_close = False

            if idx < len(arr2) and arr2[idx] - x <= d:
                has_close = True
            if idx > 0 and x - arr2[idx - 1] <= d:
                has_close = True

            if not has_close:
                count += 1

        return count
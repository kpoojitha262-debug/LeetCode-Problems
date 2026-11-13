class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Reverse the array so we can use a sliding window
        nums.reverse()

        # Monotonic stack of (value, count)
        st = []
        left = 0
        cost = 0
        ans = 0

        for right in range(n):
            cnt = 1

            while st and st[-1][0] < nums[right]:
                val, c = st.pop()
                cost += (nums[right] - val) * c
                cnt += c

            st.append((nums[right], cnt))

            while cost > k:
                val, c = st[0]
                cost -= val - nums[left]
                c -= 1
                left += 1

                if c == 0:
                    st.pop(0)
                else:
                    st[0] = (val, c)

            ans += right - left + 1

        return ans
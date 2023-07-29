import sys


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_array_len = float("inf")
        current_sum = 0
        start = 0

        for i in range(len(nums)):
            current_sum += nums[i]

            while current_sum >= target:
                min_array_len = min(min_array_len, i-start+1)
                current_sum -= nums[start]
                start += 1

        return 0 if min_array_len == float("inf") else min_array_len

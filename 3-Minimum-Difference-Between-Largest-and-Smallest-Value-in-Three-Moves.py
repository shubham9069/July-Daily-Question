# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/description/


class Solution(object):
    def minDifference(self, nums):
        if len(nums) <= 4:
            return 0
        nums.sort()
        k = len(nums) - 3
        ans = nums[-1] - nums[0]
        for i in range(k - 1, len(nums)):
            ans = min(ans, nums[i] - nums[i - k + 1])
        return ans

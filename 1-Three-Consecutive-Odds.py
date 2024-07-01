# https://leetcode.com/problems/three-consecutive-odds/description/?envType=daily-question&envId=2024-07-01


class Solution(object):
    def threeConsecutiveOdds(self, arr):
        count = 0
        for elem in arr:
            if elem % 2 == 1:
                count += 1
            else:
                count = 0
            if count == 3:
                return True
        return False

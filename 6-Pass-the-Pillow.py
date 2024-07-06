# https://leetcode.com/problems/pass-the-pillow/description/?envType=daily-question&envId=2024-07-06


class Solution(object):
    def passThePillow(self, n, time):
        itrateArray = time // (n - 1)
        time = time % (n - 1)
        if itrateArray % 2 == 1:
            return n - time
        return time + 1

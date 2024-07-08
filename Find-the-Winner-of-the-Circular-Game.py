# https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/?envType=daily-question&envId=2024-07-08


class Solution(object):
    def findTheWinner(self, n, k):
        res = 0
        for player_num in range(2, n + 1):
            res = (res + k) % player_num
            print(res)
        return res + 1

# Water Bottles
# https://leetcode.com/problems/water-bottles/description/?envType=daily-question&envId=2024-07-07

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        n = numBottles
        ans = n

        while n>=numExchange :
            ans+=n // numExchange
            n = (n//numExchange) + (n % numExchange)
        return ans
        
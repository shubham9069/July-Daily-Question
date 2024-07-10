# https://leetcode.com/problems/average-waiting-time/description/?envType=daily-question&envId=2024-07-09


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        prepareTime = customers[0][0]
        sumi = 0
        for elem in customers:
            arriveTime = elem[0]
            timeTaken = elem[1]

            if arriveTime > prepareTime:
                prepareTime = arriveTime + timeTaken
            else:
                prepareTime += timeTaken
            sumi += prepareTime - arriveTime
        return sumi / len(customers)

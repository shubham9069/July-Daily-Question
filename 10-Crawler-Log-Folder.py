# https://leetcode.com/problems/crawler-log-folder/description/?envType=daily-question&envId=2024-07-10


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        noOfOperation = 0

        for elem in logs:
            if elem == "./":
                continue

            if elem == "../":
                if noOfOperation > 0:
                    noOfOperation -= 1
            else:
                noOfOperation += 1
        return noOfOperation

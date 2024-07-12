# https://leetcode.com/problems/maximum-score-from-removing-substrings/description/?envType=daily-question&envId=2024-07-12


class Solution(object):
    def maximumGain(self, s, x, y):
        stack = []
        ans = 0
        x1 = "ab"
        y1 = "ba"
        if x < y:
            y1 = x1
            x1 = "ba"
            x, y = y, x

        for elem in s:
            if stack and stack[-1] == x1[0] and elem == x1[1]:
                stack.pop()
                ans += x
            else:
                stack.append(elem)

        s = "".join(stack)
        stack = []
        for elem in s:
            if stack and stack[-1] == y1[0] and elem == y1[1]:
                stack.pop()
                ans += y
            else:
                stack.append(elem)
        return ans

# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/?envType=daily-question&envId=2024-07-11


class Solution:
    def reverse(self, startIdx, endIdx, arr):
        i = startIdx
        j = endIdx
        while i < j:
            if arr[i] == "-":
                i += 1
            if arr[j] == "-":
                j -= 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
        pass

    def reverseParentheses(self, s: str) -> str:
        strArray = list(s)
        stack = []
        for i in range(0, len(strArray)):
            if strArray[i] == "(":
                stack.append(i)
            elif strArray[i] == ")":
                self.reverse(stack[-1] + 1, i - 1, strArray)
                strArray[stack[-1]] = "-"
                strArray[i] = "-"
                stack.pop()
        result = ""
        for elem in strArray:
            if elem != "-":
                result += elem

        return result

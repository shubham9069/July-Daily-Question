# https://leetcode.com/problems/sort-the-jumbled-numbers/description/?envType=daily-question&envId=2024-07-24


class Solution(object):
    def sortJumbled(self, mapping, nums):
        mappedNums = {}
        for elem in nums:
            convertStr = str(elem)
            newStr = ""
            for ch in convertStr:
                newStr += str(mapping[int(ch)])
            mappedNums[elem] = newStr
        return sorted(nums, key=lambda x: mappedNums[x])

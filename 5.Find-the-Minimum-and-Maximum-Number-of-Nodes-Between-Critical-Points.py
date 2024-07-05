# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        # maxima track
        arr = []
        prevNodeVal = head.val
        countNode = 1
        head = head.next

        while head.next:
            countNode += 1
            if (prevNodeVal < head.val and head.val > head.next.val) or (
                prevNodeVal > head.val and head.val < head.next.val
            ):
                arr.append(countNode)
            prevNodeVal = head.val
            head = head.next

        if len(arr) < 2:
            return [-1, -1]

        minDistance = arr[1] - arr[0]
        maxDistance = arr[-1] - arr[0]

        for i in range(1, len(arr)):
            minDistance = min(minDistance, arr[i] - arr[i - 1])

        return [minDistance, maxDistance]

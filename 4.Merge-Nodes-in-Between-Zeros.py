# https://leetcode.com/problems/merge-nodes-in-between-zeros/description/?envType=daily-question&envId=2024-07-04


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def addNode(self, lastNode, nodeSum):
        updateLastNode = ListNode(nodeSum)
        lastNode.next = updateLastNode
        return updateLastNode

    def mergeNodes(self, head):

        # iterate node with head.next because head is already zero
        head = head.next
        nodeSum = 0
        lastNode = ListNode(0)  # storing the last node so we node easily in end of ans 
        ans = lastNode
        while head:
            if head.val == 0:
                lastNode = self.addNode(lastNode, nodeSum)
                nodeSum = 0
            else:
                nodeSum += head.val
            head = head.next
        return ans.next

# https://leetcode.com/problems/create-binary-tree-from-descriptions/description/?envType=daily-question&envId=2024-07-16


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def createBinaryTree(self, descriptions):
        hashnode = {}
        childNode = set()

        for elem in descriptions:
            parent = elem[0]
            child = elem[1]
            isLeft = elem[2]

            if parent not in hashnode:
                hashnode[parent] = TreeNode(parent)
            if child not in hashnode:
                hashnode[child] = TreeNode(child)

            if isLeft:
                hashnode[parent].left = hashnode[child]
            else:
                hashnode[parent].right = hashnode[child]
            childNode.add(child)
        for key in hashnode:
            if key not in childNode:
                return hashnode[key]
        return None

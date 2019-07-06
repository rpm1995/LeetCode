# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:

        def isleafnode(node):

            if not node:
                return False

            if not node.left and not node.right:
                return True

            return False

        def addleafnodes(node):

            if not node:
                return

            if isleafnode(node):
                ans.append(node.val)

            addleafnodes(node.left)
            addleafnodes(node.right)

        ans = []

        if not root:
            return ans

        if not isleafnode(root):
            ans.append(root.val)

        leftsubtreenodes = root.left

        while leftsubtreenodes:

            if not isleafnode(leftsubtreenodes):
                ans.append(leftsubtreenodes.val)

            if leftsubtreenodes.left:
                leftsubtreenodes = leftsubtreenodes.left

            else:
                leftsubtreenodes = leftsubtreenodes.right

        leafnodes = root
        addleafnodes(leafnodes)

        rightsubtreenodes = root.right
        rightplaceholder = []

        while rightsubtreenodes:

            if not isleafnode(rightsubtreenodes):
                rightplaceholder.append(rightsubtreenodes.val)

            if rightsubtreenodes.right:
                rightsubtreenodes = rightsubtreenodes.right

            else:
                rightsubtreenodes = rightsubtreenodes.left

        ans.extend(reversed(rightplaceholder))
        return ans

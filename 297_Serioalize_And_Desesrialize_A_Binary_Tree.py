# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def __init__(self):
        self.array = []

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def helper(node):

            if not node:
                self.array.append("#")
            else:
                self.array.append(str(node.val))
                helper(node.left)
                helper(node.right)

        helper(root)
        return ",".join(self.array)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        data = data.split(",")

        # print(data)

        def helper(encoded):
            # print(encoded)

            value = encoded.pop(0)

            if value == "#":
                return None

            node = TreeNode(int(value))

            node.left = helper(encoded)
            node.right = helper(encoded)

            return node

        return helper(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

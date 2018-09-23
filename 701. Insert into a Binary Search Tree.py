# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#todo: make un rep version
class Solution:
	def insertIntoBST(self, root, val):
		"""
		:type root: TreeNode
		:type val: int
		:rtype: TreeNode
		"""
		if root == None:
			endnode = TreeNode(val)
			return endnode

		if val < root.val:
			root.left = self.insertIntoBST(root.left, val)
		else:
			root.right = self.insertIntoBST(root.right, val)
		return root

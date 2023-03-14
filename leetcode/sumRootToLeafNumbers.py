# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def summation(root,total=[]):
            if root is None : return 0
            total.append(str(root.val))

            if root.right == None and root.left == None:
                return int(''.join(total))

            left = summation(root.left,[x for x in total])
            right = summation(root.right,[x for x in total])
       
            return left + right
        return summation(root)
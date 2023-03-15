# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]
        fnull = False

        while len(queue) > 0 :
            current = queue[0]
            queue = queue[1:]

            if current.left :
                if fnull : return False 
                queue.append(current.left)
            else:
                fnull = True
            if current.right : 
                if fnull : return False
                queue.append(current.right)
            else:
                fnull = True
        return True
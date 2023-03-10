# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.head = head
        self.values = []
        current = head
        while current is not None:
            self.values.append(current.val)
            current = current.next
        

    def getRandom(self):
        """
        :rtype: int
        """
        rand = random.randint(0,len(self.values)-1)
        return self.values[rand]

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
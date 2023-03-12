
import heapq
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Remove any empty linked lists from the input list
        lists = [lst for lst in lists if lst]
        
        # If there are no non-empty linked lists, return an empty list
        if not lists:
            return None
        
        # Initialize a dummy node as the head of the merged linked list
        dummy = ListNode(0)
        curr = dummy
        
        # Create a heap and populate it with the first node of each linked list
        heap = [(lst.val, lst) for lst in lists]
        heapq.heapify(heap)
        
        # While the heap is not empty
        while heap:
            # Get the smallest node from the heap
            val, node = heapq.heappop(heap)
            
            # Add the smallest node to the merged linked list
            curr.next = ListNode(val)
            curr = curr.next
            
            # If the smallest node has a next node, add it to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
        
        # Return the head of the merged linked list (i.e., the second node of the dummy node)
        return dummy.next

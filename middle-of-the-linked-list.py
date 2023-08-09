# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current=head
        count=0
        while current is not None:
            current=current.next
            count+=1
        current=head
        current_idx=1
        idx=count//2+1
        while current_idx!=idx:
            current=current.next
            current_idx+=1
            head=current
        return head
           

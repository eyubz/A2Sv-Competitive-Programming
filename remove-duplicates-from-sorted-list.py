# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        duplicateList=[]
        current=head
        prev=None
        while current is not None:
            if current.val in duplicateList:
                prev.next=current.next
                current=prev.next
            else:
                duplicateList.append(current.val)
                prev=current
                current=current.next
        return head

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        newSet=set(nums)
        for i in newSet: 
            if nums.count(i)==1:
              return i

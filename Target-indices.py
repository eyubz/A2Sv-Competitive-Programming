class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums=sorted(nums)
        indexList=[]
        for i in range(len(nums)):
            if nums[i]==target:
                indexList.append(i)
        return indexList

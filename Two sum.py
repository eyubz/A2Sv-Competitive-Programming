class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index=[]
        for i in range(len(nums)):
            j=i+1
            for j in range(j,len(nums)):
                if nums[i]+nums[j]==target:
                    index.append(i)
                    index.append(j)
                    return index

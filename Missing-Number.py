class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length=len(nums)
        for i in range(length+1):
            if i in nums:
                continue
            else:
                return i

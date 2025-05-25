class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for index in range(len(nums)):
            nums[index] = nums[index] % 2
        
        return sorted(nums)                  
        
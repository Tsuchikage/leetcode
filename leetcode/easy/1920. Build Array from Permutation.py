class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in range(0, len(nums)):
            res.append(nums[nums[num]])

        return res

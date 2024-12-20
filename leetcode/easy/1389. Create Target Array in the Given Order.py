class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """

        result = []

        for i in range(len(index)):
            result.insert(index[i], nums[i])

        return result

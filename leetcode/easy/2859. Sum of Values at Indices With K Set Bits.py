class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = 0

        for index in range(len(nums)):
            bin_num = (bin(index))[2:]

            if bin_num.count("1") == k:
                count += nums[index]

        return count
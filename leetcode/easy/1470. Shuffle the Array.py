class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        for num in range(n):
            res.append(nums[:n][num])
            res.append(nums[n:][num])
        return res

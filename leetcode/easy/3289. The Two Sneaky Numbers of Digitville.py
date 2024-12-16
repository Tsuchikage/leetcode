class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for element in nums:
            count = nums.count(element)
            if count >= 2 and element not in res:
                res.append(element)

        return res
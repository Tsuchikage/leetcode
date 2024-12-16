class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        good_pairs = 0
        for num in range(0, len(nums)):
            for num2 in range(num + 1, len(nums)):
                if nums[num] == nums[num2]:
                    good_pairs += 1
        return good_pairs

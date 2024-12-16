class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        oper_count = 0
        for num in nums:
            if num % 3 != 0:
                if (num + 1) % 3 == 0 or (num - 1) % 3 == 0:
                    oper_count += 1
        return oper_count

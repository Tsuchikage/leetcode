class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subsets = [[]]

        for num in nums:
            new_subsets = []
            for subset in subsets:
                new_subsets.append(subset + [num])
            subsets += new_subsets

        total_xor_sum = 0
        for subset in subsets:
            current_xor = 0
            for num in subset:
                current_xor ^= num
            total_xor_sum += current_xor

        return total_xor_sum

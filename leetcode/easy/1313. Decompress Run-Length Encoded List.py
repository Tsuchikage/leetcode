class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res_lst = []

        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i + 1]

            for _ in range(freq):
                temp_lst = []
                temp_lst.append(val)
                res_lst += temp_lst

        return res_lst

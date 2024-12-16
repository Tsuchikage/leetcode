class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        for hour in hours:
            if hour >= target:
                res += 1

        return res

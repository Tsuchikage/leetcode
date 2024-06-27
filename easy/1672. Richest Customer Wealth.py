class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        res = 0
        for account in accounts:
            temp = 0
            for num in account:
                temp += num

            if temp >= res:
                res = temp

        return res

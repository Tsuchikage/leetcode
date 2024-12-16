class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        res = 0
        for jw_letter in list(jewels):
            for st_letter in list(stones):
                if jw_letter == st_letter:
                    res += 1
        return res

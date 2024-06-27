class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        num_1 = 0
        num_2 = 0

        for num in range(1, n + 1):
            if num % m != 0:
                num_1 += num

            elif num % m == 0:
                num_2 += num

        return num_1 - num_2
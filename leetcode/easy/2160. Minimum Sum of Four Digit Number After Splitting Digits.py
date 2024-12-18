class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        numbers = sorted(list(str(num)))
        first_number = numbers[0] + numbers[2]
        second_number = numbers[1] + numbers[3]
        return int(first_number) + int(second_number)
class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """

        year, month, day = date.split('-')

        binary_year = bin(int(year))[2:]
        binary_month = bin(int(month))[2:]
        binary_day = bin(int(day))[2:]

        binary_date = '-'.join([binary_year, binary_month, binary_day])

        return binary_date

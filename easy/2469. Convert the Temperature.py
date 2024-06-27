class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        res = []
        res.append(celsius + 273.15)
        res.append((celsius * 1.8) + 32)

        return res
    
class Solution(object):
    def stableMountains(self, height, threshold):
        """
        :type height: List[int]
        :type threshold: int
        :rtype: List[int]
        """
        res = []
        for index in range(1, len(height)):
            if height[index - 1] > threshold:
                res.append(index)

        return res


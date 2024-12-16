class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n

        for index in range(1, n):
            leftSum[index] = leftSum[index - 1] + nums[index - 1]

        for index in range(n - 2, -1, -1):
            rightSum[index] = rightSum[index + 1] + nums[index + 1]

        answer = [0] * n
        for index in range(n):
            answer[index] = abs(leftSum[index] - rightSum[index])

        return answer


class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        letters = list(s)
        for letter in range(0, len(letters) - 1):
            res += abs(ord(letters[letter]) - ord(letters[letter + 1]))

        return res

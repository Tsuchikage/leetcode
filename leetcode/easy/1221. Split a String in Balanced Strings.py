class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = 0
        temp_str = ''
        for letter in range(len(s)):
            temp_str += s[letter]
            temp_s = s[len(temp_str):]

            if temp_str.count('R') == temp_str.count('L') and temp_s.count('R') == temp_s.count('L'):
                res += 1

        return res

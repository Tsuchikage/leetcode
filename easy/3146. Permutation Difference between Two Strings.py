class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        letters_s = list(s)
        letters_t = list(t)

        res = 0

        for letter_s in letters_s:
            for letter_t in letters_t:
                if letter_s == letter_t:
                    res += abs(letters_s.index(letter_s) - letters_t.index(letter_t))

        return res
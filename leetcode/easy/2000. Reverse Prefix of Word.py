class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch in word:
            position = word.index(ch)
            return (word[:position + 1])[::-1] + word[position + 1:]
        else:
            return word
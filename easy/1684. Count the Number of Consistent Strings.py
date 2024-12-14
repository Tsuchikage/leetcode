class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed_set = set(allowed)
        res = 0

        for word in words:
            is_consistent = True
            for char in word:
                if char not in allowed_set:
                    is_consistent = False
                    break
            if is_consistent:
                res += 1
        return res
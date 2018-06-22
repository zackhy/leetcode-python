class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        start = longest = 0

        for i, c in enumerate(s):
            if c in d and start <= d[c]:
                start = d[c] + 1
            if i - start + 1 > longest:
                longest = i - start + 1
            d[c] = i

        return longest

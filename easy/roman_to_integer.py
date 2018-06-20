class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        temp = d['M']
        out = 0
        for n in s:
            if d[n] > temp:
                out = out - 2 * temp
            out = out + d[n]
            temp = d[n]
        return out

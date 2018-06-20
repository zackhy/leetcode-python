class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            out = -1 * int(str(abs(x))[::-1])
        else:
            out = int(str(x)[::-1])
        return out if -2**31 <= out <= 2**31 -1 else 0

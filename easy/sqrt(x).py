class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        high = x
        low = 0
        while True:
            mid = (high + low) / 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            elif x < mid ** 2:
                high = mid
            else:
                low = mid + 1

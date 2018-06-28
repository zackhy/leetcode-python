class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Recursion, Time Limit Exceeded
        # if n == 0:
        #     return 1
        # elif n < 0:
        #     return 0
        # else:
        #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        if n < 3:
            return n

        a = 1
        b = 2
        for _ in range(3, n + 1):
            a, b = b, a + b

        return b

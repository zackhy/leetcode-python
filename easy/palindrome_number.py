class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Use str()
        # return str(x)[::-1] == str(x)
        # Without converting integer to a string.
        if 0 <= x < 10:
            return True
        if x < 0 or x % 10 == 0:
            return False
        else:
            temp = x
            rev = 0
            while True:
                res = temp % 10
                rev = 10 * rev + res
                temp = int(temp/10)
                if temp == 0:
                    break
            return True if rev == x else False

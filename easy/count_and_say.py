class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'

        s = self.countAndSay(n - 1)

        tmp = s[0]
        i = 0
        ret = ''

        for c in s:
            if c == tmp:
                i += 1
            else:
                ret += str(i) + tmp
                i = 1
                tmp = c

        ret += str(i) + tmp
        return ret

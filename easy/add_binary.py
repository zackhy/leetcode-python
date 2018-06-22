class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) > len(b):
            a, b = b, a

        c = ''
        flag = 0
        for i in range(1, len(a) + 1):
            curr = int(a[-i]) + int(b[-i]) + flag
            c = str(curr % 2) + c
            if curr > 1:
                flag = 1
            else:
                flag = 0

        if flag == 0:
            return b[:-len(a)] + c
        else:
            for i in range(len(a) + 1, len(b) + 1):
                curr = int(b[-i]) + flag
                c = str(curr % 2) + c
                if curr > 1:
                    flag = 1
                else:
                    return b[:-i] + c

        return '1' + c

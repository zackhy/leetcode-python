class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        for n in s[::-1]:
            if n == ' ' and length > 0:
                break
            elif n == ' ':
                continue
            else:
                length += 1

        return length

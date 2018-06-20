class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        close = {")": "(", "}": "{", "]": "["}

        open = []
        for bracket in s:
            if bracket not in close:
                open.append(bracket)
            elif len(open) == 0:
                return False
            elif close[bracket] == open.pop():
                continue
            else:
                return False

        return True if len(open) == 0 else False

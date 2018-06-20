class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s = " ".join(strs)
        spl = ""
        try:
            for c in strs[0]:
                spl = spl + c
                temp = s.split(" " + spl)
                if len(temp) == len(strs):
                    continue
                else:
                    spl = spl[:-1]
                    break
        except:
            pass

        return spl

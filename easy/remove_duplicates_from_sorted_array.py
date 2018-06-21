class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = None
        i = 0

        for n in nums:
            if n != unique:
                unique = n
                nums[i] = unique
                i = i + 1

        return i

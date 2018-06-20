class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for idx, n in enumerate(nums):
            if target - n in d:
                return [d[target - n], idx]
            d[n] = idx
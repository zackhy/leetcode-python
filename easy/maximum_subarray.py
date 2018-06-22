class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        prev = maxium = nums[0]
        for n in nums[1:]:
            prev = max(prev + n, n)
            maxium = max(prev, maxium)

        return maxium

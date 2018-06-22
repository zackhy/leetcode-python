class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(digits) + 1):
            if digits[-i] + 1 < 10:
                digits[-i] += 1
                return digits
            else:
                digits[-i] = (digits[-i] + 1) % 10

        digits.insert(0, 1)
        return digits

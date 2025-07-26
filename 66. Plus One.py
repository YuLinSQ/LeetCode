class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1
        while i >= 0:
            if digits[i]+1 == 10:
                digits[i] = 0
                i-=1
            else:
                digits[i] = digits[i]+1
                return digits
        if digits[0] == 0:
            digits.append(0)
            digits[1:] = digits[0:-1]
            digits[0] = 1
        return digits
        

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 2
        if n < 2:
            return n
        if n == 2:
            return 2
        for i in range(n-2):
            temp = b
            b = a+b
            a = temp
        return b

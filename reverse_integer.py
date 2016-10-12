import math

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max = math.pow(2,31)
        if x >= 0: flag = 1
        else: flag = -1
        _ = str(abs(x))
        reverse = _[::-1]
        result = int(reverse)
        if flag == -1: 
            result = result * (-1)
        if  result > max or result < -max: 
            result = 0
        return result
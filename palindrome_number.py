class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        result = False
        s = str(x)
        l = len(s)
        if l == 1: return True
        for i in range(l/2):
            if s[i] == s[-(i+1)]:
                result = True
            else:
                result = False
                break
        return result

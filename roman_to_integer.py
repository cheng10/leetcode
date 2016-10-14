class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1,000
        I, V, X, L, C, D, M = 1, 5, 10, 50, 100, 500, 1000
        
        if s == '':
            return 0
            
        res = eval(s[-1])
        
        i = len(s)-2
        while i >= 0:
            if eval(s[i]) < eval(s[i+1]):
                res -= eval(s[i])
            else:
                res += eval(s[i])
            i -= 1
        
        return res

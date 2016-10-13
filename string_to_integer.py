class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        flag = 1
        result = 0
        
        if str == '': return 0
        if str[0] == '+':
            str = str[1:]
        elif str[0] == '-':
            str = str[1:]
            flag = -1
        
        for i in str:
            if i < '0' or i > '9':
                break
            result = result * 10 + int(i)
            if result > (1 << 31):
                result = (1 << 31)
                break
                    
        result *= flag
        if result > ((1 << 31)-1):
            result = ((1 << 31)-1)
        if result < (-1 * (1 << 31)):
            result = (-1 * (1 << 31))
            
        return result

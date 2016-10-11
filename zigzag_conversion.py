class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        cycle = 2*(numRows-1)
        if numRows == 1: cycle = 1
        map = []
        for i in range(numRows):
            map.append('')
            
        for j in range(len(s)):
            mod = j % cycle
            if mod < numRows:
                map[mod] += s[j]
            else:
                map[2*(numRows-1)-mod] += s[j]
                
        result = ''
        for i in range(numRows):
            result += map[i];
            
        return result

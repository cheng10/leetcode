class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = ''
        min_len = 0
        
        if len(strs) == 0:
            return ''
            
        if len(strs) == 1:
            return strs[0]
            
        for i in strs:
            if len(i) == 0:
                return ''
            
        min_len = len(min(strs, key=len))
            
        for i in range(min_len) :
            for j in range(len(strs)-1):
                if strs[j][i] == strs[j+1][i]:
                    if j == (len(strs)-2):
                        common += strs[j][i]
                else:
                    return common
            
        return common   

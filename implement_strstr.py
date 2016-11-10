class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '' or needle == haystack:
            return 0
            
        if len(needle) > len(haystack):
            return -1
            
        res = []
        for s in range(len(haystack)):
            p = 0
            for i in range(s, len(haystack)):
                if needle[p] == haystack[i]:
                    p += 1
                else:
                    p = 0
                if p == (len(needle)):
                    res.append(i-len(needle)+1)
                    break
        
        if len(res) == 0:
            return -1

        return min(res)

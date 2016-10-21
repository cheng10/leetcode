class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pare = {')':'(', ']':'[', '}':'{'}
        stack = []
        
        for i in s:
            try: 
                if i == '(' or i == '[' or i == '{':
                    stack.append(i)
                elif stack.pop() == pare[i]:
                    continue
                else:
                    return False
            except IndexError:
                return False
                
        if stack == []:    
            return True
        else: 
            return False

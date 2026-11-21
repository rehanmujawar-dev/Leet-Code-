class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ascii_code=[0]*26
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            ascii_code[ord(s[i])-ord('a')]+=1
            ascii_code[ord(t[i])-ord('a')]-=1
        
        for i in ascii_code:
            if i!=0:
                return False
           
        return True


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum=0
        for i in range(len(s)-1): 
            if s[i] in hash:
                if hash[s[i]]<hash[s[i+1]]:
                    sum-=hash[s[i]]
                else:
                    sum+=hash[s[i]]
        sum+=hash[s[-1]]
        return sum
        
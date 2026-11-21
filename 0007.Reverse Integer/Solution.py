class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign=-1 if x<0 else 1
        x=abs(x)        
        original=x
        digit=0
        while(x>0):
            reminder=x%10
            digit=digit*10+reminder
            x=x//10
        digit=digit*sign
        if digit<-2**31 or digit>2**31-1:
            return 0
        return digit
       
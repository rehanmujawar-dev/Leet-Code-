class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        list=[]
        for element in s:
            list.append(element)
        left=0
        right=len(s)-1

        while left<right:
            if list[left] in "aeiouAEIOU":
                if list[right] in "aeiouAEIOU":
                    list[left],list[right]=list[right],list[left]
                    right-=1
                    left+=1
                else:
                    right-=1
            else:
                left+=1
        ans=""
        for i in list:
            ans+=i
        
        return ans

    
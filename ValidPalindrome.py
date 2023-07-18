class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        newText=''
        for i in s:
            if i.isalnum():
                newText+=i;
        rev=newText[::-1]
        if newText==rev:
            return True
        return False
    

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        list1=list(s)
        count=0
        for i in t:
            if i in list1:
                list1.remove(i)
                count+=1
        if count==len(s) and len(s)==len(t):
            return True
        return False



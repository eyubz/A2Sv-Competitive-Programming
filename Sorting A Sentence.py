class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        text={}
        initial=0
        for i in s:
            if i.isdigit():
                text[i]=s[initial:s.index(i)]
                initial=s.index(i)+2
        text=dict(sorted(text.items()))
        s=''
        for i in text.keys():
            s+=text[i]+' '
        s=s.rstrip()
        return s

class Solution:
    def addSpaces(self, s, spaces) -> str:
        newStr=''
        start=0
        for sp in spaces:
            newStr+=s[start:sp]
            newStr+=" "
            start=sp
        newStr+=s[spaces[-1]:]
        return newStr

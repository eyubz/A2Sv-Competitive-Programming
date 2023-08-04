class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=0
        end=0
        substr=set()
        maxlen=0
        while end<len(s):
            if s[end] not in substr:
                substr.add(s[end])
            else:
                maxlen=max(maxlen,end-start)
                while s[end] in substr:
                    substr.remove(s[start])
                    start+=1
                substr.add(s[end])
            end+=1
        maxlen=max(maxlen,end-start)
        return maxlen

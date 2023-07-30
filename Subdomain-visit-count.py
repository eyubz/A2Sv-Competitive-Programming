class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        new_dict={}
        for i in cpdomains:
            list1=i.split()
            cost=int(list1[0])
            count=len(list1[1])-1
            while count>=0:
                if list1[1][count]==".":
                    newStr=list1[1][count+1:len(list1[1])]
                    if newStr in new_dict:
                        new_dict[newStr]+=cost
                    else:
                        new_dict[newStr]=cost
                count-=1
            if list1[1] in new_dict:
                 new_dict[list1[1]]+=cost
            else:
                 new_dict[list1[1]]=cost
        ns=''
        l=[]
        for i in new_dict:
            ns=str(new_dict[i])+" "+i
            l.append(ns)
        return l

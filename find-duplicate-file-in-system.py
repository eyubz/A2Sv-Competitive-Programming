class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        root=[]
        result=[]
        new_dict={}
        for i in paths:
            path=i.split()
            r=path[0]
            del path[0]
            for j in path:
                for k in j:
                    if k=="(":
                        content=j[j.index(k)+1:len(j)-1]
                        new_dict[r+"/"+path[path.index(j)][0:j.index(k)]]=content
        sets=set(new_dict.values())
        l=list(new_dict.values())
        for i in sets:
            arr=[]
            val=l.count(i)
            if val>1:
                for k in new_dict:
                    if new_dict[k]==i:
                        arr.append(k)
                result.append(arr)
        return result   

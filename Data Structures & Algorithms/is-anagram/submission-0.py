class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        symbols1 = dict()
        symbols2 = dict()
        for i in s:
            if i in set(symbols1.keys()):
                symbols1[i]+=1
            else:
                symbols1[i]=1
        for j in t:
            if j in set(symbols2.keys()):
                symbols2[j]+=1
            else:
                symbols2[j]=1
        if len(symbols1)!=len(symbols2):
            return False
        else:
            for i in symbols1:
                if symbols2.get(i) is None:
                    return False
                if symbols1.get(i) != symbols2.get(i):
                    return False
        return True
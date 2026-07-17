class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            s_sort=sorted(s)
            t_sort=sorted(t)
            return s_sort==t_sort
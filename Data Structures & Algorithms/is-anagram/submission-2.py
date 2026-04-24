class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) >= len(t):
            l = list(t)
            for ch in s:
                if ch in l:
                    l.remove(ch)
                else:
                    return False
            return True
        if len(t) > len(s):
            l = list(s)
            for ch in t:
                if ch in l:
                    l.remove(ch)
                else:
                    return False
            return True
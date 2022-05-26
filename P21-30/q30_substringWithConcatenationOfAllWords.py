class Solution(object):
    def match(self,s,dict,size):
        i = 0
        while i <= len(s)- size:
            tmp = s[i:i + size]
            if tmp in dict and dict[tmp] != 0:
                dict[tmp] -= 1
            else:
                return False
            i += size
        return True
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        sizew = len(words)
        if sizew == 0:
            return []
        d = {}
        ans = []
        for i in words:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        j = 0
        ss = len(s); sw = len(words[0])
        while j <= ss - sizew * sw:
            tmpd = d.copy()
            if self.match(s[j:j + sizew * sw],tmpd,sw):
                ans.append(j)
            j += 1
        return ans
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        ctw = {}
        wtc = {}
        for i in range (len(pattern)):
            if pattern[i] in ctw and ctw[pattern[i]] != words[i]:
                return False
            if words[i] in wtc and wtc[words[i]] != pattern[i]:
                return False
            ctw[pattern[i]] = words[i]
            wtc[words[i]] = pattern[i]
        return True

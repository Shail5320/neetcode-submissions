class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        s = ""
        while i<len(word1) and i<len(word2):
            s+=word1[i]
            s+=word2[i]
            i+=1
        s+= word2[i:] + word1[i:]
        return s
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashDict = {}
        for word in strs:
            hashList = [0] * 26
            for letter in word:
                hashList[ord(letter) - 97] += 1
            key = tuple(hashList)
            if key not in hashDict:
                hashDict[key] = []
            hashDict[key].append(word)
        return list(hashDict.values())
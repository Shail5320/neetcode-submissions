class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        key = strs[0]
        for s in strs[1:]:
            while not s.startswith(key):
                key = key[:-1]
                if not key:
                    return ""
        return key
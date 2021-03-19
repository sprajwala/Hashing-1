# Time Complexity: O(n) where n is the len of the string
# Space Complexity: O(n) worst case when each element of s has to be mapped to each elelment of t

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # edge
        if len(s) == 1:
            return True
        
        hash_map = {}
        for i in range(len(s)):
            if s[i] not in hash_map:
                
                if t[i] in hash_map.values():
                    return False
                else:
                    hash_map[s[i]] = t[i]
            else:
                if hash_map[s[i]] != t[i]:
                    return False
        return True
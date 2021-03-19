# Time Complexity: O(n k ) where k is the len of the string and n is the number of words
# Space Complexity: O(k) where k is the number of unique anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            hash_map[tuple(count)].append(s)
            
        return hash_map.values()
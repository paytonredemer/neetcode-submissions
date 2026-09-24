class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            counts = [0] * 26
            for letter in word:
                counts[ord(letter) - ord('a')] += 1
            key = tuple(counts)
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
        return list(anagrams.values())
 
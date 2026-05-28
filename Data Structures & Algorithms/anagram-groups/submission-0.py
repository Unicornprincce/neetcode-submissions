class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for i in range(len(strs)):

            sorted_word = ''.join(sorted(strs[i]))

            if sorted_word in hashmap:
                hashmap[sorted_word].append(strs[i])

            else:
                hashmap[sorted_word] = [strs[i]]

        return list(hashmap.values())  

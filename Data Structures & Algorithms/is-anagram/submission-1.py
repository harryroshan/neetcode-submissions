class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap = {}
        t_hashmap = {}
        for letter in s:
            if letter in s_hashmap:
                s_hashmap[letter] += 1
            else:
                s_hashmap[letter] = 1
        for letter in t:
            if letter in t_hashmap:
                t_hashmap[letter] += 1
            else:
                t_hashmap[letter] = 1
        if len(s_hashmap) != len(t_hashmap):
            return False
        for key in s_hashmap:
            if key not in t_hashmap or s_hashmap[key] != t_hashmap[key]:
                return False
        return True
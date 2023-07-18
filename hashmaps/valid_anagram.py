class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hash_map1 = {}
        hash_map2 = {}
        x = 1

        if s == t:
            return True

        if len(s) != len(t):
            return False

        for i in t:
            if i not in s:
                return False

        for i in sorted(s):
            if i not in hash_map1:
                x = 1
                hash_map1[i] = 1

            else:
                x += 1
                hash_map1[i] = x
        l = 1

        for f in sorted(t):
            if f not in hash_map2:
                l = 1
                hash_map2[f] = 1

            else:
                l += 1
                hash_map2[f] = l

        array1 = []
        array2 = []

        for i in hash_map1.values():
            array1.append(i)

        for i in hash_map2.values():
            array2.append(i)

        if array1 == array2:
            return (True)
        else:
            return (False)

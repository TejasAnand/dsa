class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hash_map = {}

        for i in nums:

            if i not in hash_map:
                hash_map[i] = 1

            else:
                hash_map[i] += 1

        if max(hash_map.values()) == 1:
            return False
        else:
            return True


# implementation with hashsets

        hash_set = set()

        for i in nums:
            if i in hash_set:
                return True
            else:
                hash_set.add(i)

        return False

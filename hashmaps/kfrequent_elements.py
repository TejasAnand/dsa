class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash_map = {}
        x = 1

        for i in sorted(nums):
            if i not in hash_map:
                x = 1
                hash_map[i] = 1
            else:
                x += 1
                hash_map[i] = x

        # print((hash_map.values())

        # now we need the key associated with these values in the       array
        val = []
        array = []
        sorted_repititions = sorted(hash_map.values(), reverse=True)

        array = sorted_repititions[:k]

        for key, value in hash_map.items():

            if value in array:
                val.append(key)

        return val

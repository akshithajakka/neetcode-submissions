class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        uniqueHash = {}

        for i in range(len(nums)):
            uniqueHash[nums[i]] = 1 + uniqueHash.get(nums[i], 0)

        sorted_uniqueHash = dict(sorted(uniqueHash.items(), key=lambda item: item[1], reverse=True))

        return list(sorted_uniqueHash)[:k]


        
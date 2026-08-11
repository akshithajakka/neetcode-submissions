class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffHash = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in diffHash:
                return [diffHash[complement], i]
            
            diffHash[nums[i]] = i
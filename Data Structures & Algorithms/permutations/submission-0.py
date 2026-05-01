class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2:
            return [nums]
        result = []
        for i in range(len(nums)):
            for p in self.permute(nums[:i] + nums[i+1:]):
                result.append([nums[i]] + p)
        return result
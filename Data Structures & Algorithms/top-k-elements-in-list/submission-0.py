class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for n in nums:
            if n not in nums_dict:
                nums_dict[n] = 1
            else:
                nums_dict[n] += 1
        most_freq = []
        while k > 0:
            most_freq.append(max(nums_dict, key=nums_dict.get))
            nums_dict.pop(max(nums_dict, key=nums_dict.get))
            k -= 1
        return most_freq
        
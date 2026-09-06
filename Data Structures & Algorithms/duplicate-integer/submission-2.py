class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 1:
            return False
        track = {}
        
        for num in nums:
            track[num] = track.get(num, 0) + 1 # So if the key doesn't exist, we make it zero than add one. Else, we get the value and still add 1. Meaning the default value for new key is 1
            if (track[num]) > 1:
                return True
        return False
        


        
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 1:
            return False
        track = {}
        
        for num in nums:
            track[num] = track.get(num, 0) + 1
            if (track[num]) > 1:
                return True
        return False
        


        
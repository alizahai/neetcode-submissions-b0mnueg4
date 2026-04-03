class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        if len(nums) > 0:
            prev = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == prev:
                return True
            prev = nums[i]
        
        return False
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # Brute Force
        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue
                res[i] *= nums[j]
        
        return res

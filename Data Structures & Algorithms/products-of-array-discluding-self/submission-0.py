class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        for i in range(n):
            prod = 1

            # multiply all except first element
            for j in range(1, n):
                prod *= nums[j]
            
            res[i] = prod

            # rotate left by 1 (so next element becomes excluded)
            first = nums[0]
            for k in range(n - 1):
                nums[k] = nums[k + 1]
            nums[n - 1] = first
            
        return res

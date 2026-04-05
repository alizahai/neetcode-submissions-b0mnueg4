class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1

        # store prefix product of each element at its index
        for i in range(1, n):
            prefix *= nums[i - 1]
            res[i] = prefix
        
        postfix = 1

        # calculate postfix prod of each element and 
        # multiply by prefix at that position (res[i])
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

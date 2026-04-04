class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countOfNumbers = {} # key: number, value: count
        frequency = [[] for i in range(len(nums) + 1)] # index: count, value: list of numbers with count = index

        for n in nums:
            countOfNumbers[n] = countOfNumbers.get(n, 0) + 1
        
        for num, count in countOfNumbers.items():
            frequency[count].append(num)
        
        res = []

        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                res.append(n)
                if len(res) == k:
                    return res
                    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countOfNumbers = {} # key: number, value: count
        minHeap = []

        for n in nums:
            countOfNumbers[n] = countOfNumbers.get(n, 0) + 1
        
        for num, count in countOfNumbers.items():
            heapq.heappush(minHeap, (count, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []

        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        
        return res
                    
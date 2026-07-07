class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

    # Stage 1: count frequencies
        for num in nums:
            count[num] = count.get(num, 0) + 1

    # Stage 2: sort by frequency, descending
        sorted_pairs = sorted(count.items(), key=lambda x: x[1], reverse=True)

    
# Stage 3: take top k, extract just the numbers
        result = []
        for i in range(k):
        
            result.append(sorted_pairs[i][0])
        return result
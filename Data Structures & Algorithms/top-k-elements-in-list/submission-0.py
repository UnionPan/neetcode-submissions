class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums:
            if n in freqs:
                freqs[n] += 1
            else:
                freqs[n] = 1
        sorted_keys = sorted(freqs, key=lambda k: -freqs[k])

        return sorted_keys[:k]
            
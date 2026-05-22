class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = []
        for n in nums:
            self.add(n)
        

    def add(self, val: int) -> int:
        if len(self.stream) < self.k:
            heapq.heappush(self.stream, val)
        elif val > self.stream[0]:
            heapq.heapreplace(self.stream, val)
        return self.stream[0]        

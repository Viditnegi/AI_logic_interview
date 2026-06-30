import heapq
def kthLargest(nums, k):

    n = len(nums)

    h = []
    for num in nums:
        while len(h) > k:
            heapq.heappop(h)
        
        heapq.heappush(h, -num)



    return -heapq.heappop(h)



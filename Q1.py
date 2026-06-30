def find_peak_element(nums):
    n = len(nums)
    start = 0
    end = n-1

    if len(nums) == 1:
        return 0

    while start<=end:
        mid = start + (end-start)/2
        if mid == n-1 and nums[mid-1] > nums[mid]:
            end = mid -1
        elif mid == 0 and nums[mid+1] < nums[mid]:
            start = mid+1
        elif nums[mid]>=nums[mid+1] and nums[mid]>=nums[mid-1]:
            return mid
        elif nums[mid]>=nums[mid+1]:
            end = mid-1
        else:   
            start = mid+1
        
    return -1
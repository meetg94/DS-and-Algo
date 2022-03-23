def searchInsert(nums, target):
    l, r = 0, len(nums) -1
    
    while l <= r:
        mid = (r + l)//2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            l = mid + 1
        elif target < nums[mid]:
            r = mid - 1
    return l

searchInsert([1,3,5,6], 5)
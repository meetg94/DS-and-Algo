def containsDuplicate(nums):
    hashset = set()
    
    for n in nums:
        if n in hashset:
            return True
        hashet.add(n)
    return False
        
containsDuplicate([1,2,3])
def two_sum(nums,target):
    prev_map = {} #value :index
    
    for i,n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return[prev_map[diff],i]
        prev_map[n] = i
    return
print(two_sum([1,2,3,5],4))
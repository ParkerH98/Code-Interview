def two_sum(input, target):
    prev = {}
    
    for i, n in enumerate(input):
        diff = target - n
        
        if diff in prev:
            return [ prev[diff] , i]
    
        prev[n] = i
        
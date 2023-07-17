def mergesort(input):
    
    size = len(input)
    
    if size > 1:
        
        mid = size // 2
        
        left = input[: mid]
        right = input[mid:]
        
        mergesort(left)
        mergesort(right)

        l = 0
        r = 0
        i = 0
        
        left_size = len(left)
        right_size = len(right)
        
        while l < left_size and r < right_size:
            if (left[l] < right[r]):
                input[i] = left[l]
                l +=1
            else:
                input[i] = right[r]
                r += 1
            
            i += 1
            
        while l < left_size:
            input[i] = left[l]
            l +=1
            i += 1
            
        while r < right_size:
            input[i] = right[r]
            r += 1
            i += 1
            

# x = [5, 3, 8, 22, 2, 6, 1, 7, 9, 12, 22, 13]
x = [4, 3, 6, 3, 5, 9, 2, 5, 3, 1, 6, 9, 0, 5, 4, 6, 2, 8]

mergesort(x)

print(x)
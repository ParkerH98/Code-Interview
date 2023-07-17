def common_element(input):
    table = {}
    max_occ = -1
    common_elem = -1
    
    for item in input:
        
        if item not in table:
            table[item] = 1
        else:
            table[item] += 1
        
        if max_occ < table[item]:
            max_occ = table[item]
            common_elem = item
            
    return table[common_elem]
            
            
l = [3, 4, 3, 7, 2, 1, 8, 6, 8, 2, 8, 8]
print(common_element(l))

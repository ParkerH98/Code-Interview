def change(amount):
    count = 0
    rem = amount % 25
    count += (amount - rem) / 25
    amount = rem
    
    rem = amount % 10
    count += (amount - rem) / 10
    amount = rem
    
    rem = amount % 5
    count += (amount - rem) / 5
    amount = rem
    
    count += rem / 1
    return count

print(change(69))
def isPalindrome(x):
    x = str(x)
    size = len(x)
    mid = size // 2
    stack = []
    
    if size % 2 == 0:
        for i in range(0, mid):
            stack.append(x[i])
        for i in range(mid, len(x)):
            if x[i] == stack[-1]:
                stack.pop()
            else:
                return False
            
    else:
        for i in range(0, mid):
            stack.append(x[i])
        for i in range(mid + 1, len(x)):
            if x[i] == stack[-1]:
                stack.pop()
            else:
                return False
        
    return True

print(isPalindrome(112211))
print(isPalindrome(12345654321)) 
print(isPalindrome(1234565432)) 


def match(str):
    stack = []
    answer = None
    
    lookup = {')': '(', ']': '[', '}': '{'}
    
    for char in str:
        
        # if an opening symbol
        if char in lookup.values():
            stack.append(char)
        elif stack and lookup[char] == stack[-1]:
            stack.pop()
        else:
            return False
    return True

print(match("({[]})"))
print(match("({[]}})"))

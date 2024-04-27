from collections import deque

def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    d = deque()
    for ch in s:
        d.append(ch)
    
    while len(d) > 1:
        if(d.pop() != d.popleft()):
            return False
    
    return True

print(is_palindrome("Anna"))  # True
print(is_palindrome("level"))  # True
print(is_palindrome("Hello"))  # False
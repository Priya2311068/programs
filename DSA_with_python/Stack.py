# USING A LIST AS A STACK 

s = []
s.append('HFT')
s.append('UHY')
s.append('HVG')
s.append('HGN')

s.pop()
s.pop()
s.pop()
s.pop()

print(s)

from collections import deque
stack = deque()
class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    

str = "We will conquere COVID-19"
words = str.split(' ')
print(words)
new_str = []
for word in words:
    new_word = word[::-1]
    new_str.append(new_word)
    new_str.reverse()
print(new_str)

print(" ".join(new_str))


from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    

def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ''
    while stack.size()!=0:
        rstr += stack.pop()

    return rstr

print(reverse_string("We will conquere COVI-19"))

def is_match(ch1, ch2):
    match_dic = {
        "}" : "{",
        "]" : "[",
        ")" : "("
         }
    return match_dic[ch1] == ch2
def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0


if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))

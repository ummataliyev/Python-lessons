class Stack:
    def __init__(self) -> None:
        self.elements = []
    

    def push(self, element):
        self.elements.append(element)
    

    def pop(self):
        return self.elements.pop()
    

    def top(self):
        return self.elements[-1]
    

    def size(self):
        return len(self.elements)
    
    
    def empty(self):
        return self.size() == 0


stack = Stack()
assert stack.size() == 0, f"Actual: {stack.size()}, Expected: 0"
assert stack.empty() == True, f"Actual: {stack.empty()}, Expected: True"

stack.push("Alice")
assert stack.size() == 1, f"Actual: {stack.size()}, Expected : 1"
assert stack.empty() == False, f"Actual: {stack.empty()}, Expected: False"
assert stack.top() == "Alice", f"Actual: {stack.top()}, Expected: Alice"

stack.push("Bob")
assert stack.size() == 2, f"Actual: {stack.size()}, Expected : 2"
assert stack.empty() == False, f"Actual: {stack.empty()}, Expected: False"
assert stack.top() == "Bob", f"Actual: {stack.top()}, Expected: Bob"

assert stack.pop() == "Bob", f"Actual: {stack.pop()}, Expected: Bob"

assert stack.size() == 1, f"Actual: {stack.size()}, Expected : 1"
assert stack.empty() == False, f"Actual: {stack.empty()}, Expected: False"
assert stack.top() == "Alice", f"Actual: {stack.top()}, Expected: Alice"

assert stack.pop() == "Alice", f"Actual: {stack.pop()}, Expected: Alice"
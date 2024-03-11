#햇갈렸는데 어차피 Output이 null이 되기전까진 input이 들어오든 pop() 이나 peek()연산은 동일
from collections import deque

class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
            

    def empty(self) -> bool:
        return self.input == [] and self.output == []
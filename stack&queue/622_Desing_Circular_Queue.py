class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.rear] is None:
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.front] is None:
            return False
        else:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.maxlen
            return True

    def Front(self) -> int:
        if self.q[self.front] is None:
            return -1
        else:
            return self.q[self.front]
#index에 -1 하면, 만약 self.rear = 0 일 때 제일 마지막 Index [-1] = [4]을 가리킴
    def Rear(self) -> int:
        if self.q[self.rear - 1] is None:
            return -1
        else:
            return self.q[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.rear == self.front and self.q[self.front] is None
        #이렇게 하는 것 보단 위에게 낫다
        #is 와 ==의 차이
        #https://swfungineer.medium.com/%ED%8C%8C%EC%9D%B4%EC%8D%AC-is%EC%99%80-%EC%9D%98-%EC%B0%A8%EC%9D%B4-is%EC%9D%98-%EC%82%AC%EC%9A%A9-d0bd44915017
        # if self.rear == self.front and self.q[self.front] == None:
        #     return True
        # else:
        #     return False

    def isFull(self) -> bool:
        return self.rear == self.front and self.q[self.front] is not None
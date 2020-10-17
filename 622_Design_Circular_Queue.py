class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.array = [0 for _ in range(k)]
        self.cur_size = 0
        self.capacity = k
        self.head = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.cur_size == self.capacity:
            return False

        tail = (self.head + self.cur_size) % self.capacity
        self.array[tail] = value
        self.cur_size += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.cur_size == 0:
            return False

        self.head += 1
        self.cur_size -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.cur_size == 0:
            return -1

        return self.array[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.cur_size == 0:
            return -1

        tail = (self.head + self.cur_size - 1) % self.capacity
        return self.array[tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.cur_size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.cur_size == self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

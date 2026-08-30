list = []
list.insert(0, 234)
list.insert(0, 239)
list.insert(0, 834)
list.insert(0, 764)
list.insert(0, 354)
list.insert(0, 2344)
print(list)

list.pop()
print(list)
list.pop()
print(list)
list.pop()
print(list)
list.pop()
print(list)


q = deque()
q.appendleft(5)
q.appendleft(34)
q.appendleft(56)
q.appendleft(78)
print(q)


from collections import deque
import time
import threading
class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer)==0:
            print("queue is empty ")
            return
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
    def front(self):
        return self.buffer[-1]
    
q = Queue()   
def place_order(order_list):
   
    for order in order_list:
        print("placing order for :" , order)
        q.enqueue(order)
        time.sleep(0.5)
        
    print(q)
 
def serving_order():
    time.sleep(1)
    while True: 
     order = q.dequeue()
     print("serving order for : ", order )
     time.sleep(2)
    

if __name__ =='__main__':
    order_list = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target = place_order, args = (order_list,))
    t2 = threading.Thread(target = serving_order)
    t1.start()
    t2.start()

def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for i in range(n):
        front = numbers_queue.front()
        print("   ", front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()


if __name__ == '__main__':
    produce_binary_numbers(10)

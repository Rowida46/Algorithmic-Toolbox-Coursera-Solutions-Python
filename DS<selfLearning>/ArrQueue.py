class ArrQueue:
    # we need first determine the Queue capacity as a static var >> arr circle
    capacity = 6
    def __init__(self):
        self.arr = [None]*ArrQueue.capacity
        self.front = 0
        self.size =0
        self.tail = -1
    
    def deQueue(self):
        # to dequeue :> to remove and return the first element
        # there is 4 steps requires to dequeue
        # 1>---------- first to store the val of the first element
        val = self.arr[self.front]
        # 2 >---------to make set first index as a null val
        self.arr[self.front] = None
        # 3>----------- to change the front position <circule arr>
        self.arr[self.front] = (self.front) % len(self.arr) # to increament
        # 4 >------- to decreament the size val of arr
        self.size-=1
       ## return the var  
        return val
    def enQueue(self , data):
        # to enqueue is to increament both the size and the tail by one and to append the new item
        # append > gonna add the new item at the end of the arr
        avail= (self.front + self.size) % len(self.arr)
        self.arr[avail] = data
        self.tail +=1
        self.size+=1
            ## to deal with the circular arr
        if self.tail == ArrQueue.capacity :
            self.tail =-1    
    def __len__(self):
        return len(self.arr)
    def isEmpty(self):
        return len(self.arr)==0
    def front(self):
        # to return the first element
        return self.arr[self.front]
que =ArrQueue()
que.enQueue(9)
que.arr[:que.size]






















'''


from queue import Queue 
q = Queue(maxsize = 3) 
print(q.qsize()) 
# Adding of element to queue 
q.put('a') 
q.put('b') 
q.put('c') 
print("\nFull: ", q.full()) 

# Removing element from queue 
print("\nElements dequeued from the queue") 
print(q.get()) 
print(q.get()) 
print(q.get()) 

# Return Boolean for Empty 
# Queue 
print("\nEmpty: ", q.empty()) 

q.put(1) 
print("\nEmpty: ", q.empty()) 
print("Full: ", q.full()) 
'''
'''

queue = [] 
queue.append('a') 
queue.append('b') 
queue.append('c') 
  
print("Initial queue") 
print(queue) 
# pop(0)    >>>>>>---------- to pop the fisrt element 
print(queue.pop()) 
print(queue.pop(0)) 
print(queue.pop(0)) 
  
print("\nQueue after removing elements") 
print(queue)    
        
        
'''

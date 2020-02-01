
''' 
<<< Implementing a Stack with a Singly Linked List >>>
'''

class LinkedList:
   # <<<InnerClass>>
    class Node :
        __solts__= 'element'  ,  'next' 
        def __init__(self ,element,  Next ,):
            self.next = Next
            self.element = element
    def __init__(self):
        self.head = None  # >> if list the stack is empty its head point to null
        self.size =0
    def __len__(self):
        return self.size
    def isEmpty(self):
        return self.size ==0
    def push(self , e):
        # >>>1 to crate a new node
        self.head = self.Node(e , self.head)
        self.size+=1
    def pead(self):
        return self.head.element
    def popAT0(self):
        # 3 steps to pop the head 
        #>>>1 to store the head lemnt 
        ans = self.head.element
        # >> 2 set head point to the next node
        self.head = self.head.next
        # >>>3 inc the size
        self.size-=1
        return ans
s =LinkedList()
s.push(6)
print(s.head.element)
print(s.head.next)
s.push(4)
print(s.popAT0())

print(s.head.element)
#---------------------------------------------------------------------



# <<<<<Implementing a Stack with a Singly Linked List >>>>

class LinkedListQue:
     # <<<InnerClass>>
    class Node :
        __solts__= 'element'  ,  'next' 
        def __init__(self ,element,  Next ):
            self.next = Next
            self.element = element
    def __init__(self):
        self.head =None
        self.tail = None
        self.size =0
    def __len__(self):
        return self.size
    def isEmpty(self):
        return self.size ==0
    def peek(self):
        return self.head.element
    def deQueue(self):
        ### to remove& return the first element
        ans = self.head.element
        self.head = self.head.next
        self.size -=1
        ### if queue is empty >>> gonna update tail to point to Null val
        if self.isEmpty():
            self.tail = None
        return ans
    def enQueue(self , e):
        '''
        to add an element to the <<BACK>> of  the Queue
        '''
        
        # >>1 first create a new Node
        newelement = self.Node(e, None)
        '''
         if the Queue is empty >> gonna set the new element as a head and tail as wll
         otherwise 
         if it's not empty  set tail point to the new element
        '''     
        if self.isEmpty():
            self.head = newelement
        else :
            self.tail.next = newelement
        self.size+=1
        self.tail == newelement
        
        
            

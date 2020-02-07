def reverse(head):
    pre = None 
    cur = head 
    nxt = cur.Next
    while cur :
        nxt= cur.Next
        cur.Next = pre
        pre = cur
        cur = nxt
    head = pre
    return head 

class Node:
    def __init__(self , data):
        self.data = data
        self.Next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def pushat0(self , data):
        node = Node(data)
        node.Next = self.head
        self.head = node

    def push(self , data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            self.tail.Next = node
        self.tail = node
        
    def insertbetween(self , data , index):
        node = Node(data)
        tmp = self.head 
        i =1
        while tmp:
            if i == index :
                node.Next = tmp.Next
                tmp.Next = node
                break
            tmp = tmp.Next
            i+=1
    def popdata(self ,e ):
        tmp=self.head       
        ## if we gonna delet the head
        if self.head.data == e :
            self.head = tmp.Next
            return 
        while tmp :
            if tmp.Next.data == e :
                tmp.Next = tmp.Next.Next
                break
            tmp = tmp.Next
        
    def deletindex(self , position):
        i=1 ; tmp = self.head
        if position ==0 :
            self.head = tmp.Next
        while tmp :
            if i == position:
                tmp.Next = tmp.Next.Next
                break
            tmp= tmp.Next
            i+=1
    
    def pop(self):
        tmp = self.head 
        while tmp :
            if tmp.Next.Next == None :
                self.tail = tmp
                tmp.Next = None
                break
            pre = tmp
            tmp = tmp.Next 
    
    def getnode(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.Next
    def reverse (self):
        tmp = self.head
        l = []
        while tmp :
            l.append(tmp.data)
            tmp = tmp.Next
        if l :
            for i in l[::-1]:
                print(i , end=' ')
            
l = LinkedList()
l.push(4) 
l.push(6)
l.push(12)
l.push(5)
l.pushat0("dana")
l.insertbetween(1 , 1)
#l.pop()
l.popdata("dana")
l.deletindex(1)
l.getnode()
l.reverse()

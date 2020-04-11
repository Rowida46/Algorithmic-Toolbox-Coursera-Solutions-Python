class Node :
    def __init__(self , data):
        self.data = data 
        self.next = None
        
        

class linkedList:
    def __init__(self):
        self.tail = None 
        self.head = None
### to <<<<< add >>>>
    def pushfront(self , key):
        node = Node(key)
        if not self.head : ### it's just an empty linkedlist
            self.head = self.tail =  node
        else :
            node.next = self.head 
            self.head = node
            
    def pushback(self , key):
        node = Node(key)
        if not self.head :
            self.head = self.tail = node
        else :
            self.tail.next = node
            self.tail = node
    def insertbetween(self , data , index):
        node = Node(data)
        tmp = self.head 
        i =1
        while tmp:
            if i == index :
                node.next = tmp.next
                tmp.next = node
                break
            tmp = tmp.next
            i+=1
            
    def CountRec(self, node): 
        if (not node): 
            return 0
        else: 
            return 1 + self.CountRec(node.next) 
  
    # A wrapper over getCountRec() 
    def getCount(self): 
        return self.getCountRec(self.head) 
##### <<<< to delet >>>>
    def popfront(self):
        if not self.head :
            return False 
        val = self.head.data
        if self.head == self.tail :
            self.tail = self.head = None
        else : 
            self.head = self.head.next
            
    def popback(self):
        if not self.head :
            return False
        if self.head == self.tail : ### there is only one element in the list
            self.head = self.tail = None
        else :
            curr = self.head
            while curr.nextnext :
                curr = curr.next
            curr.next = None
            self.tail = curr
            
    def popdata(self ,e ):
        tmp=self.head       
        ## if we gonna delet the head
        if self.head.data == e :
            self.head = tmp.next
            return 
        while tmp :
            if tmp.next.data == e :
                tmp.next = tmp.next.next
                break
            tmp = tmp.next
    def deletindex(self , position):
        i=1 ; tmp = self.head
        if position ==0 :
            self.head = tmp.next
        while tmp :
            if i == position:
                tmp.Next = tmp.next.next
                break
            tmp= tmp.next
            i+=1
    def erase(self , key):
        if not self.head :
            return False
        node = Node(key)
        curr = self.head 
        while curr.next :
            if curr.next.data == node.data :
                curr.next = curr.next.next
                return 
            curr = curr.next
#####################################################    
    def isEmpty(self):
        return (self.tail and self.head) == None
    def topfront(self):
        return self.head.data
    def topback(self):
        return self.tail.data
   
    def find(self , key):
        if not self.head :
            return False
        node = Node(key)
        curr = self.head
        while curr :
            if curr.data == node.data :
                return node.data
            curr = curr.next
        return -1
    def reverse_iterative(self):
        ### firstly ,  we gonna make head point to NONE and keep track to thenext node
        cur = self.head 
        next_node = head.next
        cur.next = None
        while next_node :
        ### our strategy is to save the next_node and play woth the current pointer
            tmp = next_node.next
            next_node.next = cur ### to make next_node point to the pre node
            head = cur = next_node
            next_node = tmp
    def tostring(self):
        cur = self.head 
        i = 0 
        while cur !=None :
            print(i , cur.data)
            cur = cur.Next
            i+=1
   
    
    def getnode(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.Next

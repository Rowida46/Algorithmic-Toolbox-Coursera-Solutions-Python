class Node:
    def __init__(self , val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self ):
        self.head = None
        self.tail = None
        self.size = -1
    def push(self , v):
        self.size+=1
        node = Node((v , self.size))
        if not self.head:
            self.head = self.tail = node
        else :
            self.tail.next = node
            self.tail = node

    def pop_val(self , v):
        if v == self.head.val :
            self.head = self.head.next
        tmp = self.head.next
        while tmp.next:
            if tmp.next.val == v :
                tmp.next = tmp.next.next
                return 
            tmp = tmp.next
    def pop(self):
        i = 0
        tmp = self.head
        while  i < self.size-1:
            tmp = tmp.next
            i+=1
        self.tail = tmp
        self.tail.next = None
    
    def __iter__(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next
class HashMap:
    
    def __init__(self , n):
        self.liken_hash_map = [0 for i in range(n)]
        self.taple_size = n
    
    def put(self ,k , v):
        hash_fun = k % self.taple_size
        if self.liken_hash_map[hash_fun] == 0 :
            self.liken_hash_map[hash_fun] = LinkedList()
            self.liken_hash_map[hash_fun].push(v)
        else:
            self.liken_hash_map[hash_fun].push(v)
    
    def itr(self , k):
        self.liken_hash_map[k % self.taple_size].__iter__()
    
    def remove(self , k):
        hash_fun = k % self.taple_size
        if self.liken_hash_map[hash_fun] == 0 :
            return None
        self.liken_hash_map[hash_fun].pop()
        
hashmap = HashMap(5)           
hashmap.put(15 , 'dana')
hashmap.put(15 , 'rowida')
hashmap.put(15 , 'dana')
hashmap.put(15 , 'rowida')
hashmap.itr(5)

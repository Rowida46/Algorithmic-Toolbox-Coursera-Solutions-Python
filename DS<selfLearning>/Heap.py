class Heap:
    ### max heap
    def __init__(self):
        self.size = -1
        self.heap = []
        self.max_size = 13
    
    def parent(self , i):
        return i//2
   
    def right_child(self , i ):
        return i//2 + 2
    
    def left_child(self , i ):
        return i//2 +1
    
    def Shiftup(self , i ):
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.heap[i] , self.heap[i//2] = self.heap[i//2] , self.heap[i]
            i = i//2
    
    def Shiftdown(self , i):
        max_index = i 
        l , r = i//2 + 1  , i//2 + 2
        ### to to know with which dirction we've to swap
        ### as we have to firstly compare with left direction >>>> the bigest
        if l <= self.size and self.heap[l] > self.heap[maxindex]:
            maxindex = l 
        if r <= self.size and self.head[r] > self.heap[maxindex] :
            maxindex = r
        if i != maxindex :
            self.heap[i] , self.heap[maxindex] = self.heap[maxindex] , self.heap[i]
            self.Shitdown(maxindex)
    
    def insert(self , val) :
        if self.size == self.maxsize :
            return None
        self.size += 1
        self.head.append(val)
        self.Shiftup(self.size)
    def ExtractMax(self):
        val = self.heap[0]
        self.heap[0] = self.heap[self.size]
        self.size -= 1
        self.Shiftup(self.size)
        return val
    def remove(self , i):
        self.heap[i] = float('inf')
        self.Shiftup(i)
        self.ExtractMax()
    
    def ChangePriority(self , i , p):
        oldp = self.heaap[i]
        self.heap[i] = p
        if oldp > p :
            self.Shiftdown(i)
        else :
            self.Shiftup(i)
    
    def Buildeheapsort(self):
        for i in range(self.size//2 , 1 , -1):
            self.Shiftdown(i)
    
    def HeapSort(self):
        self.Buildeheapsort()
        tmp = self.size
        for i in range(self.size-1):
            self.heap[i] , self.heap[tmp] =  self.heap[i],self.heap[tmp]
            tmp -=1
            self.Shiftdown(i)
            
    def PartialSorting(self , k): 
        ###### Running time: O(n + k log n)
        for i in range(k):
            self.ExtractMax()
            

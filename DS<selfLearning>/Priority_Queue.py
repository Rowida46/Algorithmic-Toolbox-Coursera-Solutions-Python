class Priority_Queue :
    def __init__(self , root):
        self.root = root
        self.rightchild = None 
        self.leftchild = None
        self.parent = None
        self.size = 0
        self.max_size = 13
        self.H = ['0'] * self.max_size
        
    def parent(i):
        return i//2
    def leftchild(i):
        return 2 * i
    def rigthchild(i):
        return 2*n +1
    
    def siftup(self , i ):
        while i > 0 and self.H[i]  > self.H[i//2]:
            ## to swap 
            tmp = self.H[i]
            self.H[i] = self.H[i//2]
            self.H[i//2] = tmp
            i //=2 ## i = self.parent(i)
    
    def siftdown(self , i):
#-----------------------------------------------------------------------------------------------------------------------
        ### we first need to select the directionof SIFTING based on the child that has large val
        max_index = i 
        l = self.leftchild(i) 
        if l <= self.size and self.H[l] > self.H[max_index]:
            max_index = l
        ###same with the rightchild
        r = self.rigthchild(i) 
        if r <= self.size and self.H[r] > self.H[max_index]:
            max_index = r
#-----------------------------------------------------------------------------------------------------------------------
        if i != max_index :
            ### to swap
            tmp = self.H[i]
            self.H[i] = self.H[max_index]
            self.H[max_index] = tmp
            self.siftdown(max_index) ### to keep SIFTING
            
    def insert(self , p):
        ### to first checkif there a space to
        if self.size == self.max_size :
            raise IndexError 
            
        self.size+=1 
        self.H[size] = p
        self.siftup(size)
    def extract_MAX(self):
        res = self.H[0] ### to store the root
        self.H[0] = self.H[self.size] ## to make root equal to last leaf
        size-=1 ## to dec the size as we gonna lose an elemen >>node
        self.siftdown(0)
        return res
    
    def remove(self , p):
        self.H[p] =  'inf' #### i forget how to asign inf to a val rightnow , DAMN
        self.siftup(p)
        self.extract_MAX()
    
    def change_priority(self , i , p):
        oldp = self.H[i] ### to strore the old priority
        self.H[i] = p ### to chamge the priority >>> assign the priority to the new one
        ### to keep tracking of a balanc tree >> we gonne either sift (up : dow) based on oldp > ? < p
        if oldp < p:
            self.siftup(i)
        else:
            self.siftdown(i)

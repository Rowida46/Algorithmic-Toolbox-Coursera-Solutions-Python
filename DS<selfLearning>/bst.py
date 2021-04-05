class Node :
    def __init__(self , data):
        self.data = data 
        self.rightchild = None
        self.leftchild = None
    
class Tree: ## binary search tree<<<<<BST>>>>
    def __init__(self):
        self.root = None
    def insert(self , data):
        node =  Node(data)
        if not self.root : ## it's an empty tree
            self.root = node
        else :
            curr = self.root
            parent = None ### to keep track of the following root
            while True :
                parent = curr 
                if parent.data > data:
                    curr = curr.leftchild
                    if not curr :
                        parent.leftchild = node
                        return
                else :
                    curr = curr.rightchild
                    if not curr:
                        parent.rightchild = node
                        return
        
    def get_parent_with_node(self , data): ### tp detect which node and parent we gonna paly with
        curr = self.root 
        parent = None
        if not curr: ###en empty tree
            return parent , None
        while True :
            if curr.data == data :
                return (parent , curr)
            elif curr.data > data :
                parent = curr
                curr =  curr.leftchild
            else :
                parent = curr
                curr = curr.righthild
        return (parent , curr)
    
    
    def delet(self , data):
        parent , node = self.get_parent_with_node(data)
        if not node and not parent :
            return False
        ## to determine with case we are in 
        child_no = 0
        if node.rightchild and node.leftchild:
            child_no = 2
        elif not node.rightchild or not node.leftchil :
            child_no = 1
        else :
            child_no = 0
#---------------------<<<case1>>>>><<<no child>>>>--------------
        if child_no == 0 :
            if parent : ### not root
                if parent.leftchild == node :
                    parent.rightchild = None
                else :
                    parent.rightchild = None
            else :
                self.root = None
#---------------------<<<case2>>>>><<<one child>>>>--------------
        elif child_no == 1 :
            next_node = None
            if node.leftchild :
                next_node = node.leftchild
            else :
                next_node = node.rightchild
            if parent :
                if parent.leftchild == node:
                    parent.leftchild = next_node
                else :
                    parenct.rightchild = next_node
            else:
                self.root = next_node
#---------------------<<<case3>>>>><<<2 children>>>>--------------
       ### else :
        ###not yet
    
    def inorder(self):
        curr = self.root
        if not curr :
            return 
        self.inorder(curr.leftchild)
        print(curr.data)
        self.inorder(curr.rightchild)
        
    def preorder(self):
        curr = self.root
        if not curr :
            return 
        print(curr.data)
        self.inorder(curr.leftchild)
        self.inorder(curr.rightchild)
        
    def preorder_indented(self  , data , depth):
        # Print preorder representation of subtree of T rooted at p at depth d
        """
            Paper                   Paper
            Title                     Title
            Abstract                  Abstract
            $ 1                         $ 1
            $ 1.1                         $ 1.1
            $ 1.2                         $ 1.2
            $ 2                         $ 2
            $ 2.1                         $ 2.1
            ...                         ...        
           """

        """
        def preorder indent(T, p, d):
        
            2 Print preorder representation of subtree of T rooted at p at depth d
            3 print(2 d + str(p.element( ))) # use depth for indentation
            4 for c in T.children(p):
            5 preorder indent(T, c, d+1)
            
            ex : preorder indent(T, T.root( ), 0)
        """
        p , node = elf.get_parent_with_node(data)
        #  use depth for indentation
        if node :
            print(2 * d + " " + str(node))
            
        # # child depth is d+1
        if node.leftchild:
            return preorder_indented(self  , data.leftchild , depth+1)
        if node.rightchild:
             return preorder_indented(self  , data.leftchild , depth+1)

    def postorder(self):
        curr = self.root
        if not curr :
            return
        print(curr.data)
        self.inorder(curr.leftchild)
        self.inorder(curr.rightchild)
        
    def next_larger(self , x):
        ## Mit 6-006 lec 5
        parent , node = self.get_parent_with_node(x)
        if node.rightchild :
            return node.rightchild
        else :
            while parent:
                """
                
                while y not NIL and x = right(y)
                x = y; y = parent(y)
                return(y);
                while y = parent , x = data & node
                """"
                parent , node = self.get_parent_with_node(parent)
                
            return parent
        
        
    def BFS(self):
        Q = [self.root]
        list_of_nodes = []
        while Q :
            node = Q.pop(0)
            list_of_nodes.append(node.data)
            if node.leftchild :
                list_of_nodes.append(node.leftchild)
            if node.rightchild :
                list_of_nodes.append(node.rightchild)
        return list_of_nodes
    
    def find_min(self):
        curr = self.root
        while curr.leftchild:
            curr = curr.leftchild
        return curr
    
    def find_max(self):
        curr = self.root
        while curr.rightchild :
            curr = curr.rightchild
        return curr
    
    def search(self , data):
        curr = self.root
        while True :
            if not curr :
                return False
            elif curr.data == data :
                return data
            elif curr.data > data :
                curr = curr.leftchild
            else :
                curr = curr.rightchild
        return -1

    def LeftDescendant(Self , node):
        if not node.leftchild :
            return node
        else :
            return self.LeftDescendant(node.leftchild)
        
    def RightAncestor(self , node):
        if not node.rightchild :
            return node
        else :
            return self.RightAncestor(node.rightchild)
        
    def AdjacentElements(self , node): ### coursera week 5 slide3
        if not node.leftchild :
            return RightAncestor(node.rightchild)
        else:
            return LeftDescendant(node.leftchild)
        
    def RangeSearch(self , x , y):
        list_of_inRange_elements = []
        node = self.search(x)
        while node.data <= y :
            if node.data >= x:
                list_of_inRange_elements.append(node)
            node = self.AdjacentElements(node)
        return list_of_inRange_elements
    

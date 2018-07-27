class Node:
    #initialize class
    def __init__(self,data,next_node = None):
        self.data = data
        self.next_node = next_node
    #getters and setters
    def get_data(self):
        return self._data
    
    def set_data(self,value):
        self._data = value
        
    data = property(get_data,set_data)
    
    def get_next(self):
        return self._next_node
    
    def set_next(self,new_node):
        self._next_node = new_node
        
    next_node = property(get_next,set_next)
    
    ########
    
class LinkedList:
    #initialize class
    def __init__(self,root,last = None,length = 1):
        self.root = root
        self.last = root
        self.length = 1
    #getters and setters    
    def get_root(self):
        return self._root
    
    def set_root(self,value):
        self._root = value
        
    data = property(get_root,set_root)
    
    def get_last(self):
        return self._last
    
    def set_last(self,value):
        self._last = value
        
    last = property(get_last,set_last)
   
    def get_length(self):
        return self._length
    
    def set_length(self,value):
        self._length = value
        
    length = property(get_length,set_length)
    #insert a value. length increases, last node becomes the inserted node.
    def insert(self,new_node):
        self.last.next_node = new_node
        self.last = new_node
        self.length+=1
    #remove a value. length should decrement.
    #last node should stay the same, or change to the next to last node
    #root node should stay the same, or change to the next to first node
    def remove(self,remove_value):
        pointer = self.root
        runner = self.root.next_node
        if pointer.data == remove_value:
                self.root = runner
            
        while TRUE: 
            if runner.data == remove_value:
                pointer.next_node = runner.next_node
            
        
        
        
        
        
a = Node(1)
b = Node(10)
c = Node(100)

LL = LinkedList(a)
print(LL.root.data)
print(LL.last.data)
LL.insert(b)
print(LL.root.data)
print(LL.last.data)
print(LL.length)
    
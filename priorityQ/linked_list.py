### what are my data structures 
class Node:
    val = ""
    priority = 0
    next = None 
    prev = None 
    def __init__(self, val, priority):
        self.val = val 
        self.priority = priority
        return 

class LinkedList:
    head = None 
    tail = None 
    size = 0 
    file = ""
    
    def add(self, val, priority):
        node = Node(val, priority)
        self.size+=1
        if self.head == None:
            self.head = node 
            return
        curr = self.head
        if self.head.next == None:
            self.head.next = node 
            return 
        if node.priority < curr.priority:
            self.head = node 
            node.next = curr 
            return 
        while curr.next != None:
            if node.priority >= curr.next.priority:
                 curr = curr.next
                 continue
            if node.priority < curr.next.priority:
                node.next = curr.next
                curr.next = node 
                return 
        curr.next = node 
        return 
    
    def ll_index(self, number):
        ### 1 2 3 4 
        if number == 0:
            return self.head
        number -= 1
        if number > self.size or number < 0:
            return None 
        
        node = self.head
        while number != 0:
            node = node.next 
            number -= 1
        return node 

    def head_pop(self, number):
        if number > self.size:
            number = self.size
        ret = []
        for i in range(number):
            node = self.ll_index(i+1)
            val, p = node.val, node.priority 
            ret.append("p" + str(p)+":   " + val)
        return ret
    
    def remove(self, number):
        if number <= 1:
            node = self.head.next 
            self.head = node 
            self.size -= 1
            return 
        node = self.ll_index(number)
        prev = self.ll_index(number-1)
        prev.next = node.next 
        self.size -= 1
        return 
    
    
    def pop(self):
        if self.head == None:
            return "queue is empty"

        node = self.head 
        self.remove(1)
        self.add(node.val, node.priority)
        return "back of priority line:      " + ("item 1: p" + str(node.priority) + ":    " + node.val)
    
    def print(self):
        if self.head == None:
            return "queue is empty"

        node = self.head 
        ret = []
        for i in range(self.size):
            ret.append("item " + str(i+1) + "     p" + str(node.priority) + ":    " + node.val)
            node = node.next
        return ret
    
    def print_1_2(self):
        if self.head == None:
            return "queue is empty"

        node = self.head 
        ret = []
        for i in range(self.size):
            if node.priority > 1:
                return ret 
            ret.append("item " + str(i+1) + "     p" + str(node.priority) + ":    " + node.val)
            node = node.next
        return ret
    
    def change_priority(self, number, new_priority):
        node = self.ll_index(number)
        if node == None:
            return node 
        self.remove(number)
        node.priority = new_priority
        self.add(node.val, new_priority)
        return 1
    
    def rename(self, number, name):
        node = self.ll_index(number)
        node.val = name 
        return 

    def clear(self, file):
        writefile = open(file, "w")
        writefile.write("")
        writefile.close()
        self.head = None 
        self.tail = None 
        self.size = 0 
    
    def from_file(self, lines):
        ll = LinkedList()
        for i in lines:
            priority = int(i[-1])
            val = i[:-1]
            ll.add(val, priority)
        return ll 
    
    def to_file(self, file):
        writefile = open(file, "w")
        node = self.head 
        while node != None:
            line = node.val+str(node.priority)+"\n"
            writefile.write(line)
            node = node.next
        writefile.close()





    
    
    
    
    
            
        

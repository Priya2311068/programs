# LINKED LIST IMPLEMENTATION IN PYTHON

class Node:
    def __init__(self, data = None, next = None ):
        self.data = data
        self.next = next

class Linked_list:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("linked list is empty!!")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+ ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        
        return count
    
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
    
    def remove_at(self, index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1


    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data) 


    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            raise Exception("Linked list is empty")
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                return
            itr = itr.next
        raise Exception(f"value{data_after} not found in the Linked List")
    
    def remove_by_value(self, data):
        if self.head == None:
            raise Exception("linked list is empty")
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr:
            if itr.next and itr.next.data == data:
                itr.next = itr.next.next
                return
    
if __name__ =='__main__':
    ll = Linked_list()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()


# DOUBLY LINKED LIST IMPLEMENTATION IN PYTHON
class doublynode:
    def __init__(self, data = None, next = None, prev = None):
        self.data= data
        self.next = next
        self.prev = prev

class doubly_linked_list:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("doubly linked list is empty!!")
            return
        itr = self.head
        llstr =''
        while itr:
            llstr += str(itr.data) + ' <-> ' if self.next else str(itr.data)
            itr = itr.next
        print(llstr) 

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def insert_at_begining(self, data):
        node = doublynode(data, self.head, None)
        if self.head is not None:
            self.jead.prev = node
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = doublynode(data, None, None)
            return
        itr = self.head
        while itr:
            if itr.next is None:
                node = doublynode(data, None, itr)
                itr.next = node
                break
            itr = itr.next

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("invalid index")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0 
        itr = self.head
        while itr:
            if count == index - 1:
                node = doublynode(data, itr.next, itr)
                if itr.next is None:
                    self.insert_at_end(data)
                else:
                    itr.next.prev = node
                    itr.next = node
                    break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index > self.get_lenbgth():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                if itr.next is not None:
                    itr.next = itr.next.next
                    if itr.next is not None:
                        itr.next.prev = itr
                    else:
                        itr.next = None

                else:
                    itr.next = None
                break
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_values(self, data_after, data_to_insert):
        if self.head is None:
            raise Exception("Doubly Linked List is Empty")
        itr = self.head
        while itr:
            if itr.data == data_after:
                Node= doublynode(data_to_insert, itr.next, itr)
                if itr.next is not None:
                    itr.next.prev = Node
                    itr.next = Node
                else:
                    itr.next = Node
                    Node.prev = itr
                return
            itr = itr.next
        raise Exception(f"Value {data_after} not found in the Doubly lisked list")

    def print_reverse(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' <-> ' if itr.prev else str(itr.data)
            itr = itr.prev
        print(llstr)

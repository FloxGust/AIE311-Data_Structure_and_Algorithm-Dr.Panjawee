class Node :
    def __init__ (self, value) :
        self.value = value
        self.nextvalue = "" #'None'

class LinkedList :
    
    #initial node value
    def __init__ (self): 
        self.Header = "" #'None'

    #Append from last position
    def append(self, value):
        if self.Header != "":
            self = self.Header
        while self.nextvalue != "":
            self = self.nextvalue
        self.nextvalue = Node(value)

List_A = LinkedList()
List_A.Header = Node(4)
List_A.append(10)


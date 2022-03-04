class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class Linked_list:
    def __init__(self):
        self.head = None
    
    def insert_at_beggnining(self,data):
        node=Node(data,self.head)
        self.head=node

    def prints(self):

        if self.head is None:
            print('list is empty')
            return
         
        itr=self.head
        LstStr=''
        while itr:

            LstStr +=str(itr.data)+'---->'
            itr=itr.next

        print(LstStr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        
        itr=self.head

        while itr.next:
          
            itr=itr.next
        
        itr.next=Node(data,None)
    
    def insert_values(self,data_list):
        self.head=None
        
        for data in data_list:
            self.insert_at_end(data)
       
    def length(self):
        length=0
        itr=self.head

        while itr:
            length=length+1
            itr=itr.next

        print('leng: ',length)
        
    def remove_data(self,data):

        itr=self.head
        if(itr.data == data):
            self.head=itr.next
            return
       
        
        while itr and itr.next.data != data:
            print(itr.data)
            itr=itr.next
        itr.next=itr.next.next

    def remove_by_index(self,index):
        itr=self.head
        if index ==0:
            self.head=itr.next
        for i in range(index-1):
           itr=itr.next
        
        if itr.next.next :itr.next=itr.next.next

        
    def add_element_by_index(self,data,index):
        itr=self.head
        if index ==0:
            new_node=Node(data,itr)
            self.head=new_node
            return
        for i in range(index-1):
            itr=itr.next
        
        
        new_node=Node(data,itr.next)
        itr.next=new_node

        

ll=Linked_list()

ll.insert_values([22,44,675,345,77,123])
ll.remove_by_index(123)
ll.prints()
ll.add_element_by_index(233,3)
ll.prints()
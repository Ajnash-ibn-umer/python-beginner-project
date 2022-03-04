class Node:
    def __init__(self,data,next,prev):

        self.data=data
        self.next=next
        self.prev=prev

class DblikedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def add_value_end(self,data):
        itr=self.head
        if self.head is None:
            self.head=Node(data,self.tail,None)
            return
        while itr.next:
            itr=itr.next
        new_node=Node(data,None,itr)
        self.tail=new_node
        itr.next=new_node

    def print_list(self):
        itr=self.head
        while itr:
            print(itr.data,'<--->',end='')
            itr=itr.next
    def print_list_reverse(self):
        itr=self.tail
        while itr:
            print(itr.data,'<--->',end='')
            itr=itr.prev

    def add_values(self,data_list):
        self.head=None
        for data in data_list:
            self.add_value_end(data)
        


dl=DblikedList()
values=([22,354,456,6878,9,678])
dl.add_values(values)
dl.print_list_reverse()







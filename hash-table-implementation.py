

from xml.etree.ElementTree import Element


class hash_table:

    def __init__(self):
        self.MAX=100
        self.arr=[[] for i in range(self.MAX)]

    
    def get_hashcode(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.MAX
    
    def setitem(self,key,value):

        hashKey=self.get_hashcode(key)

        found =False

        for idx, element in enumerate(self.arr[hashKey]):
            if len(element)==2 and element[0] is key:
                self.arr[hashKey][idx]=(key,value)
                found = True
                break
            
        if not found:
            self.arr[hashKey].append((key,value))

    def getitem(self,key):
        hashkey=self.get_hashcode(key)
        for elm in self.arr[hashkey]:
            if elm[0]==key:
                return elm[1]
            
        
    def deleteitem(self,key):
        hashcode =self.get_hashcode(key)
        self.arr[hashcode]=None

    def print_table(self):
        for i in range(100):
            print(self.arr[i])



t=hash_table()
t.setitem('manu',5)
t.setitem('manu',22)
print(t['manu'])

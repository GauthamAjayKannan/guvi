class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.size=0
        self.head=None
    def insert(self,data,po):
        print("insertion")
        self.size=self.size+1
        newnode=node(data)
        if self.head==None:
            self.head=newnode
            if po>1:
                print("Since list is empty,insertion is done at beginning")
        elif po==1:
            newnode.next=self.head
            self.head=newnode
        else:
            temp=1
            currentnode=self.head
            while True:
               if temp==po:
                   print("Insertion done",temp)
                   newnode.next=currentnode.next
                   currentnode.next=newnode
                   break
               temp=temp+1
               currentnode=currentnode.next
            print("Invalid position")
            self.size=self.size-1
    def traverse(self):
        print("traverse")
        print(self.size)
        po=1
        if self.head==None:
            print("List is empty")
        else:
            currentnode=self.head
            while currentnode!=None:
                print(currentnode.data,po)
                po=po+1
                currentnode=currentnode.next
    def deletion(self,pos):
        if self.head==None:
            print("list is empty")
        elif pos==1:
            prev=self.head
            head=prev.next
        else:
            tem=2
            prev=self.head
            currentnode=prev.next
            while currentnode !=None:
                if tem==pos:
                    prev.next=currentnode.next
                    break
            prev=currentnode
            currentnode=currentnode.next
d=linkedlist()
d.insert(9,99)
d.insert(8,99)
d.insert(5,2)
d.traverse()

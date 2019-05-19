 class Node:
        def __init__(self,data):
            self.data=data
            self.next=None
    class linkedlist:
        def __init__(self):
            self.head=None
        def insertAtBeginning(self,data):
            newnode=Node(data)
            if self.head==None:
                self.head=newnode
            else:
                newnode.next=self.head
                self.head=newnode
        def insertAtEnd(self,data):
            newnode=Node(data)
            if self.head==None:
                self.head=newnode
            else:
                temp=self.head
                while temp.next!=None:
                    temp=temp.next
                temp.next=newnode
        def insertAtMiddle(self,data,k):
            newnode=Node(data)
            if self.head==None:
                self.head=newnode
            else:
                temp=self.head
                while temp.data!=k:
                    temp=temp.next
                newnode.next=temp.next
                temp.next=newnode
        def deleteatbeginning(self):
            if self.head==None:
                print("Linked List is empty no deletion could be done")
            else:
                first=self.head
                self.head=first.next
        def deletionatend(self):
            if self.head==None:
                print("Linked list is empty")
            else:
                prev=None
                temp=self.head
                while temp.next!=None:
                    prev=temp
                    temp=temp.next
                prev.next=None
        def deletionAtMiddele(self,data):
            if self.head==None:
                print("Linked list is empty")
            else:
                prev=None
                temp=self.head
                while temp.data!=data:
                    prev=temp
                    temp=temp.next
                prev.next=temp.next
        def traverse(self):
            if self.head==None:
                print("linked list is empty")
            else:
                temp=self.head
                while temp!=None:
                    print(temp.data)
                    temp=temp.next
    a=linkedlist()
    a.insertAtBeginning(3)
    a.insertAtEnd(10)
    a.insertAtBeginning(200)
    a.insertAtMiddle(100,3)
    a.traverse()
    print("-------")
    a.deleteatbeginning()
    a.traverse()
    print("---------")
    a.deletionatend()
    a.traverse()
    print("-----------")
    a.insertAtBeginning(99)
    a.insertAtBeginning(234)
    a.deletionAtMiddele(3)
    a.traverse()

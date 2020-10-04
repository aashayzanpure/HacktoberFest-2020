

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class ll :
    def __init__(self):
        self.head = None
    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.data,end = " ")
            
            printval = printval.next


ll1 = ll()
ll1.head = Node(1)
e2 = Node(2)
e3 = Node(3)
ll1.head.next = e2
e2.next = e3


ll2= ll()
ll2.head = Node(5)
e2 = Node(2)
e3 = Node(3)
ll2.head.next = e2
e2.next = e3

ll3=ll()
ll3.head = Node(0)
e2 = Node(0)
e3 = Node(0)
ll1.head.next = e2
e2.next = e3

ll1.listprint()
print("\n")
ll2.listprint()
print("\n")


printval = ll1.head
printval1 = ll2.head
printval2 = ll3.head
while printval is not None and printval1 is not None:
    printval.data = printval.data + printval1.data
    printval = printval.next
    printval1 = printval1.next


ll1.listprint()
print("\n")

class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.next = None


head = Employee('Emma',21)
head.next = None
def traverse(head):
    ptr = head
    while ptr!= None:
        print('The color of the car is {}.'.format(ptr.name))
        ptr = ptr.next

print('Finish traverse!')
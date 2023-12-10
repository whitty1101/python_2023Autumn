class Car:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        self.next = None
# Initiate the first element of single linked list.


red = Car('Amy','25')
red.next = None

blackcar=Car('Eddy','25')
blackcar.next=None

red.next=blackcar
blue=Car('Esme','33')
blue.next=None
blackcar.next=blue


def traverse(head):
    ptr = head
    while ptr!= None:
        print('The name of the employee is {}.'.format(ptr.name))
        print('The age of the emploryee is {}.'.format(ptr.age))
        ptr = ptr.next




traverse(red)
print('Finish traverse!')
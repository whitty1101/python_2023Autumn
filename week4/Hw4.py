class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.next = None

class Car:
    def __init__(self, color):
        self.color=color
        self.next = None
head = Car('red')
head.next = None
def traverse(head):
    ptr = head
    while ptr!= None:
        print('The color of the car is {}.'.format(ptr.color))
        ptr = ptr.next

print('Finish traverse!')
class Car:
    def __init__(self, color):
        self.color=color

head = Car('red')
second = Car('blue')
head.next=second
second.next=head

def traverse(head):
    ptr = head
    while ptr!= None:
        print('The color of the car is {}.'.format(ptr.color))
        if ptr.next == head:
            break
        ptr=ptr.next
    print('Finish traverse!')

new=Car('black')
new.next=head
ptr=head
while ptr.next!=head:
    ptr=ptr.next
ptr.next=new
    
head=new


pink=Car('pink')
pink.next=second
second.next=head
head.next.next=pink



traverse(head)
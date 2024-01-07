class members:
    def __init__(self, name, times):
        self.name=name
        self.times=times

head = members('Brian','1')
second = members('Leo','17')
third=members('John','10')
fourth=members('Amy','8')
head.next=second
second.next=third
third.next=fourth
fourth.next=head

def traverse(head):
    ptr = head
    while ptr!= None:
        print('The name of the member is {},'.format(ptr.name),'the purchase time is {}'.format(ptr.times))
        if ptr.next == head:
            break
        ptr=ptr.next
    print('Finish traverse!')
    
traverse(head)

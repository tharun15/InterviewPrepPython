from linkedlist import Node

def cycle_check(node):

    pointer1 = node
    pointer2 = node


    while pointer1 != None and pointer2.nextnode != None:
        pointer1 = pointer1.nextnode
        pointer2 = pointer2.nextnode.nextnode
        if pointer1.value == pointer2.value :
            return True
    return False

a = Node(1)
b = Node(2)
c = Node(3)


a.nextnode = b
b.nextnode = c
c.nextnode = a
print(cycle_check(a))
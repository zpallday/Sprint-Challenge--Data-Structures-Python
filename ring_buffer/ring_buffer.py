from doubly_linked_list import DoublyLinkedList
# This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age
# Ring 
# first in first out
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None 
        self.storage = DoublyLinkedList()



#  It a data queue
# Linear
# The first element is remove from head. When the head pointer gets to the end of the
# array it wraps around the first element in that array.
    def append(self, item):
        # starts the ring
            if self.capacity > self.storage.length:
               self.storage.add_to_tail(item)
               self.current = self.storage.head
 # if the capacicty an current isn't at head, then it removes it from head, and add it to tail
            elif self.capacity == self.storage.length:
                delete_this = self.storage.head
                self.storage.remove_from_head()
#if at capacity and current is at the head; move current to tail
                self.storage.add_to_tail(item)
#if not at capacity; add to tail
                if delete_this == self.current:
                    self.current = self.storage.tail
# 
    pass

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        start_node = self.current
        list_buffer_contents.append(start_node.value)
 # returns all of the elements in the buffer in a list in their given order.
        if start_node.next is not None:
            next_node = start_node.next
        else:
            next_node = self.storage.head
        while next_node != start_node:
            list_buffer_contents.append(next_node.value)
            if next_node.next is not None:
                next_node = next_node.next
            else:
                next_node = self.storage.head
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

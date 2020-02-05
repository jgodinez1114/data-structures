#################################    singly-linked-list.py    ##############################
#
# initial interface for a singly linked list
#
# Purpose: implement a Stack data structure using a singly linked list
#        
# Programmer: Joel Godinez
#
############################################################################################


# node
class SLNode:
    def __init__(self, value, next):
        self.value = value    # work with current active object
        self.next  = next     # work with current active object

# singly linked list for a stack implementation
class SLList:
    def __init__(self):

        # set header node to "start" as the sentinel
        self.header = SLNode("start", None)

    # adding elements to the stack
    def add_to_stack(self, value):

        # use temporary variable for adding a node
        temp = SLNode(value, None)

        # check if list is empty
        if self.header.next is None:
            self.header.next = temp
        else:
            temp.next = self.header.next
            self.header.next = temp

def main():
    
    # create a linked list to model the stack
    my_list_obj = SLList()

    print(type(my_list_obj))

main()


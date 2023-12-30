#!/usr/bin/python3
"""linked list Module"""


class Node:
    """
    This a Node class that create
    a node of linked list
    """
    def __init__(self, data, next_node=None):
        """
        initialize the variable of node

        Args:
            self: The instance of node
            data: the data of node
            next_node = The pointer to next node
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.data = data
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.next_node = next_node

    @property
    def data(self):
        """get data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter next_node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This is linked list class"""
    def __init__(self):
        """Initialize just head"""
        self.__head = None

    def sorted_insert(self, value):
        """function that add and sort node"""
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        temp = self.__head
        while temp.next_node is not None and temp.next_node.data < value:
            temp = temp.next_node
        new_node.next_node = temp.next_node
        temp.next_node = new_node

    def __str__(self):
        """
        function that return the element
        of linked list in string
        """
        linked_list = ""
        if self.__head is None:
            return linked_list
        current_element = self.__head
        while current_element.next_node is not None:
            linked_list += str(current_element.data) + '\n'
            current_element = current_element.next_node
        linked_list += str(current_element.data)
        return linked_list

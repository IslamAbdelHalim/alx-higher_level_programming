#!/usr/bin/python3
"""Linked list Moduel"""


class Node:
    """class node define linked list"""
    def __init__(self, data, next_node=None):
        """Initialize The variables"""
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
        """set data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set next_node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """initialize the head of linked list"""
        self.head = None

    def sorted_insert(self, value):
        """Insert and insert a new node"""
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
            return

        temp = self.head
        while temp.next_node is not None and temp.next_node.data < value:
            temp = temp.next_node

        new_node.next_node = temp.next_node
        temp.next_node = new_node

    def __str__(self):
        """print linked list"""
        linked_list = ""
        temp = self.head
        while temp:
            linked_list += str(temp.data) + "\n"
            temp = temp.next_node
        return linked_list

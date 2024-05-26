#!/usr/bin/python3
class Node:
    """
    A class that defines a node of a singly linked list.

    Attributes:
    ----------
    data : int
        The data stored in the node.
    next_node : Node or None
        The reference to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance.

        Parameters:
        ----------
        data : int
            The data to store in the node.
        next_node : Node or None, optional
            The next node in the list (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for the data attribute."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for the data attribute.

        Parameters:
        ----------
        value : int
            The new data value.

        Raises:
        ------
        TypeError:
            If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for the next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for the next_node attribute.

        Parameters:
        ----------
        value : Node or None
            The new next node.

        Raises:
        ------
        TypeError:
            If the value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class that defines a singly linked list.

    Attributes:
    ----------
    __head : Node or None
        The head of the linked list.
    """

    def __init__(self):
        """Initializes an empty SinglyLinkedList."""
        self.__head = None

    def __str__(self):
        """
        Returns a string representation of the list.

        Returns:
        -------
        str
            A newline-separated string of node data.
        """
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Parameters:
        ----------
        value : int
            The data value to insert.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

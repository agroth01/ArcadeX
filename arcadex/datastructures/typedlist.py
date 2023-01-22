class TypedList(list):
    """
    A list that only allows items of a certain type. Useful for enforcing types in lists.
    """
    def __init__(self, type : type):
        """
        Params:
            type(type): The type that the list will only allow.
        """
        self._type = type
        super().__init__()

    def append(self, item):
        """
        Appends an item to the list.

        Params:
            item(object): The item to append to the list.
        """
        if not isinstance(item, self._type):
            raise TypeError("The item is not of the correct type.")
        super().append(item)

    def extend(self, items):
        """
        Extends the list with another list.

        Params:
            items(list): The list to extend the list with.
        """
        for item in items:
            if not isinstance(item, self._type):
                raise TypeError("The item is not of the correct type.")
        super().extend(items)

    def insert(self, index, item):
        """
        Inserts an item at a certain index.

        Params:
            index(int): The index to insert the item at.
            item(object): The item to insert.
        """
        if not isinstance(item, self._type):
            raise TypeError("The item is not of the correct type.")
        super().insert(index, item)

    def __setitem__(self, index, item):
        """
        Sets an item at a certain index.

        Params:
            index(int): The index to set the item at.
            item(object): The item to set.
        """
        if not isinstance(item, self._type):
            raise TypeError("The item is not of the correct type.")
        super().__setitem__(index, item)

    def __add__(self, other):
        """
        Adds another list to this list.

        Params:
            other(list): The list to add to this list.
        """
        for item in other:
            if not isinstance(item, self._type):
                raise TypeError("The item is not of the correct type.")
        return super().__add__(other)

    def __iadd__(self, other):
        """
        Adds another list to this list.

        Params:
            other(list): The list to add to this list.
        """
        for item in other:
            if not isinstance(item, self._type):
                raise TypeError("The item is not of the correct type.")
        return super().__iadd__(other)
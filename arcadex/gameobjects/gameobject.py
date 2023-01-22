from ..datastructures import TypedList
from ..components import Component, Transform

class GameObject:
    ID_COUNTER = 0

    """
    A holder for components that are in the game. By default, a game object has a transform component.
    """
    def __init__(self, 
                name: str = "GameObject",
                tag: str = "Untagged",
                layer: int = 0):
        """
        Params:
            name(str): The name of the game object.
            tag(str): The tag of the game object.
            layer(int): The layer of the game object.
        """
        self._name = name
        self._tag = tag
        self._layer = layer

        self._components = TypedList(Component)
        self.add_component(Transform)

        self._assign_id()
    
    @property
    def id(self) -> int:
        """
        Returns the ID of the game object.
        """
        return self._id

    def has_component(self, component: type) -> bool:
        """
        Checks if the game object has a component.

        Params:
            component(type): The component to check for.
        """
        for c in self._components:
            if type(c) == component:
                return True
        return False

    def add_component(self, component: type) -> Component:
        """
        Adds a component to the game object. Will raise a TypeError if the component is not of the correct type.

        Params:
            component(type): The component to add.
        """
        c = component()
        if not issubclass(type(c), Component):
            raise TypeError("Cannot add a component that is not a subclass of Component.")

        if not c._allow_multiple:
            if self.has_component(component):
                raise TypeError("Cannot add multiple components of type {}.".format(component.__name__))

        self._components.append(c)

    def _assign_id(self):
        """
        Assigns an ID to the game object.
        """
        self._id = GameObject.ID_COUNTER
        GameObject.ID_COUNTER += 1

    def __str__(self) -> str:
        """
        Returns the name of the game object.
        """
        return self._name

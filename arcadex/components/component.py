from abc import ABC

class Component(ABC):
    """
    A component is a class that is used to add functionality to a game object.
    """
    def __init__(self,
                 allow_multiple: bool = True):
        """
        Params:
            allow_multiple(bool): Whether or not the component can be added to multiple game objects.
        """
        self._allow_multiple = allow_multiple

        self._required_components = []

    def add_required_component(self, component: type):
        """
        Adds a required component to the component.

        Params:
            component(type): The component to add.
        """
        if not issubclass(component, Component):
            raise TypeError("Cannot add a component that is not a subclass of Component as a required component.")

        self._required_components.append(component)

    @property
    def allow_multiple(self) -> bool:
        """
        Whether or not the component can be added to multiple game objects.
        """
        return self._allow_multiple
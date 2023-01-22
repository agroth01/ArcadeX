from .component import Component

class CustomClass(Component):
    """
    A custom class is a class that is used to add functionality to a game object.
    """
    def awake(self):
        """
        A method called as soon as the class is first created. Initialization that
        does not depend on any other game objects should be done here.
        """
        pass

    def start(self):
        """
        This method is called after all game objects have been created. Initialization
        that depends on other game objects should be done here.
        """
        pass

    def update(self):
        """
        Method that is called every frame.
        """
        pass
    
def require_components(components):
    """
    A decorator that is used to require components for a custom class.
    """
    def decorator(cls):
        if not issubclass(cls, CustomClass):
            raise TypeError("Cannot require components on a class that is not a subclass of CustomClass.")

        # accept both list and stand-alone component
        if not isinstance(components, list):
            components = [components]

        for component in components:
            if not issubclass(component, Component):
                raise TypeError("Cannot require a component that is not a subclass of Component.")

            cls.add_required_component(component)
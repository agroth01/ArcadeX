from .component import Component
from ..datastructures import Vector2

ALLOW_MULTIPLE = False

class Transform(Component):
    """
    A transform component is used to store the position, rotation, and scale of a game object.
    """
    def __init__(self,
                 position: Vector2 = Vector2(),
                 rotation: float = 0.0,
                 scale: Vector2 = Vector2(1.0, 1.0)):
        """
        Params:
            position(Vector2): The position of the game object.
            rotation(float): The rotation of the game object.
            scale(Vector2): The scale of the game object.
        """
        
        super().__init__(allow_multiple=ALLOW_MULTIPLE)
        self._position = position
        self._rotation = rotation
        self._scale = scale

        
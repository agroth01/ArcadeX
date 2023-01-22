from math import sqrt

class Vector2:
    """
    A 2D vector class with float values.
    """
    def __init__(self,x: float = 0.0, y: float = 0.0):
        """
        Params:
            x(float): The x component of the vector.
            y(float): The y component of the vector.
        """

        self._x = x
        self._y = y
        self._calculate_magnitude()

    # Properties

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self._calculate_magnitude()

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        self._calculate_magnitude()

    @property
    def magnitude(self) -> float:
        return self._magnitude
        
    @property
    def normalized(self) -> "Vector2":
        return Vector2(self._x / self._magnitude, self._y / self._magnitude)

    # Public methods

    def normalize(self) -> None:
        """
        Normalizes the vector.
        """
        self._x /= self._magnitude
        self._y /= self._magnitude
        self._calculate_magnitude()

    def dot(self, other: "Vector2") -> float:
        """
        Calculates the dot product of the vector and another vector.

        Params:
            other(Vector2): The other vector to calculate the dot product with.
        """
        return self._x * other.x + self._y * other.y

    def distance(self, other: "Vector2") -> float:
        """
        Calculates the distance between the vector and another vector.

        Params:
            other(Vector2): The other vector to calculate the distance to.
        """
        return sqrt((self._x - other.x) ** 2 + (self._y - other.y) ** 2)

    def angle(self, other: "Vector2") -> float:
        """
        Calculates the angle between the vector and another vector.

        Params:
            other(Vector2): The other vector to calculate the angle to.
        """
        return self.dot(other) / (self._magnitude * other.magnitude)

    # Private methods

    def _calculate_magnitude(self) -> float:
        """
        Recalculates the magnitude of the vector.
        """
        self._magnitude = sqrt(self._x ** 2 + self._y ** 2)

    # Magic methods override

    def __add__(self, other: "Vector2") -> "Vector2":
        return Vector2(self._x + other.x, self._y + other.y)

    def __mul__(self, other: float) -> "Vector2":
        return Vector2(self._x * other, self._y * other)

    def __sub__(self, other: "Vector2") -> "Vector2":
        return Vector2(self._x - other.x, self._y - other.y)

    def __str__(self) -> str:
        return f"Vector2({self._x}, {self._y})"

class Vector2Int:
    """
    A 2D vector class with integer values.
    """
    def __init__(self,x: int = 0, y: int = 0):
        """
        Params:
            x(int): The x component of the vector.
            y(int): The y component of the vector.
        """

        self._x = x
        self._y = y

    # Properties

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    # Public methods

    def distance(self, other: "Vector2Int") -> float:
        """
        Calculates the distance between the vector and another vector.

        Params:
            other(Vector2Int): The other vector to calculate the distance to.
        """
        return sqrt((self._x - other.x) ** 2 + (self._y - other.y) ** 2)

    # Magic methods override

    def __add__(self, other: "Vector2Int") -> "Vector2Int":
        return Vector2Int(self._x + other.x, self._y + other.y)

    def __mul__(self, other: int) -> "Vector2Int":
        return Vector2Int(self._x * other, self._y * other)

    def __sub__(self, other: "Vector2Int") -> "Vector2Int":
        return Vector2Int(self._x - other.x, self._y - other.y)

    def __str__(self) -> str:
        return f"Vector2Int({self._x}, {self._y})"
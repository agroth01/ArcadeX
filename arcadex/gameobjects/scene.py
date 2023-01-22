from ..datastructures import TypedList
from .gameobject import GameObject
from ..components import Component

class Scene:
    """
    A scene is a collection of game objects. This is meant to be used to organize game objects.
    Some use cases for scenes are:
        - A menu scene
        - A level scene
        - A game over scene
    """
    def __init__(self,
                name : str = "New scene") -> None:
        """
        Params:
            name(str): The name of the scene.
        """
        self._name = name
        self._game_objects = TypedList(GameObject)

    @property
    def name(self) -> str:
        """
        The name of the scene.
        """
        return self._name

    # Gameobject methods

    def add_game_object(self, game_object : GameObject) -> None:
        """
        Adds a game object to the scene.

        Params:
            game_object(GameObject): The game object to add.
        """
        self._game_objects.append(game_object)

    def remove_game_object(self, game_object : GameObject) -> None:
        """
        Removes a game object from the scene.

        Params:
            game_object(GameObject): The game object to remove.
        """
        self._game_objects.remove(game_object)

    def get_gameobject_by_id(self, id : int) -> GameObject:
        """
        Gets a game object by its ID.

        Params:
            id(int): The ID of the game object.
        """
        for game_object in self._game_objects:
            if game_object.id == id:
                return game_object
        return None

    def get_gameobject_by_name(self, name : str) -> GameObject:
        """
        Gets a game object by its name.

        Params:
            name(str): The name of the game object.
        """
        for game_object in self._game_objects:
            if game_object.name == name:
                return game_object
        return None

    def get_gameobjects_with_component(self, component : Component) -> list:
        """
        Gets a list of game objects that have a specific component.

        Params:
            component(type): The component to check for.
        """
        game_objects = []
        for game_object in self._game_objects:
            if game_object.has_component(component):
                game_objects.append(game_object)
        return game_objects

    # Magic methods override

    def __iter__(self) -> iter:
        return iter(self._game_objects)

    def __len__(self) -> int:
        return len(self._game_objects)

    def __str__(self) -> str:
        return self._name
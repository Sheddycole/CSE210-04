from casting import Actor

class Artifact(Actor):
    """A visible, moveable thing that participates in the game. 
    
    The responsibility of Artifact is to keep track of keep track of its kind, its value, and its visibility

    Attributes:
        _kind (string): The text that represents its kind
        _value (int): The value it worths
        _is_visible (boolean): if it is visible or not.
    """

    def __init__(self):
        """Constructs a new Artifact using parent's constructor"""
        super().__init__()
        self._kind = "A normal one"
        self._value = 1
        self._is_visible = True

    def get_kind(self):
        """Gets the artifact's kind.
        
        Returns:
            String: The artifact's text that represents its kind.
        """
        return self._kind

    def get_value(self):
        """Gets the artifact's value.
        
        Returns:
            integer: The artifact's value.
        """
        return self._value

    def get_visibility(self):
        """Gets the artifact's visibility.
        
        Returns:
            boolean: if the artifact is visible.
        """
        return self._is_visible

    def set_kind(self, kind):
        """Updates the kind to the given one.
        
        Args:
            kind (String): The given kind.
        """
        self._kind = kind

    def set_value(self, value):
        """Updates the value to the given one.
        
        Args:
            value (integer): The given value.
        """
        self._value = value
    
    def set_visibility(self, is_visible):
        """Updates the visibility to the given one.
        
        Args:
            is_visible (boolean): The given visibility.
        """
        self._is_visible = is_visible

'''
    # How to use this class

    # How to create GEMS

    # First example
    gem1 = Artifact()

    # We can use the '*' symbol to represent gems
    gem1.set_text("*")

    # We can set the kind of the gem like this
    gem1.set_kind("Space gem")

    # We can set its value, this will be used to increase the score of the player
    gem1.set_value(100)

    # If the gem is touched by the player, we need to set its visibility to False
    gem1.set_visibility(False)

    # Another example
    gem2 = Artifact()
    gem2.set_text("*")
    gem2.set_kind("Power gem")
    gem2.set_value(1000)
    # If the gem is touched by the player, we need to set its visibility to False
    gem2.set_visibility(False) 

    # How to create ROCKS

    # First example
    rock1 = Artifact()

    # We can use the 'o' symbol to represent rocks
    rock1.set_text("o")

    # We can set the kind of the rock like this
    rock1.set_kind("Adakite")

    # We can set its value, this will be used to decrease the score of the player
    rock1.set_value(-100)

    # If the rock is touched by the player, we need to set its visibility to False
    rock1.set_visibility(False)

    # Another example
    rock2 = Artifact()
    rock2.set_text("o")
    rock2.set_kind("Asteroid")
    rock2.set_value(-1000)
    # If the gem is touched by the player, we need to set its visibility to False
    rock2.set_visibility(False) 

'''
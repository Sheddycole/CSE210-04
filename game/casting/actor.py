from game.shared.color import Color
from game.shared.point import Point


class Actor:
    """A visible, moveable thing that participates in the game. 
    
    The responsibility of Actor is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.

    """

    def __init__(self):
        """Constructs a new Actor."""
        self._text = ""
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def get_color(self):
        """Gets the actor's color as a tuple of three ints (r, g, b).
        
        Returns:
            Color: The actor's text color.
        """
        return self._color

    def get_font_size(self):
        """Gets the actor's font size.
        
        Returns:
            Point: The actor's font size.
        """
        return self._font_size

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position
    
    def get_text(self):
        """Gets the actor's textual representation.
        
        Returns:
            string: The actor's textual representation.
        """
        return self._text

    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity
    
    def move_next(self, height, max_x, max_y):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x value.
        
        Args:
            height (int): The height of the subarea where to play.
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        up_limit = max_y - height
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = self._position.get_y() + self._velocity.get_y()
        if y < up_limit:
            y = self._position.get_y()
        elif y >= max_y:
            y = self._position.get_y()
        
        self._position = Point(x, y)

    def set_color(self, color):
        """Updates the color to the given one.
        
        Args:
            color (Color): The given color.
        """
        self._color = color

    def set_position(self, position):
        """Updates the position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position
    
    def set_font_size(self, font_size):
        """Updates the font size to the given one.
        
        Args:
            font_size (int): The given font size.
        """
        self._font_size = font_size
    
    def set_text(self, text):
        """Updates the text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity
'''
    # Example how to creat the player at the bottom of the window
    max_x = 900
    max_y = 600
    cell_size = 20
    font_size = 20
    cols = int(max_x / cell_size)
    rows = int(max_y / cell_size)
    x = int(cols / 2)
    y = rows - 1
    position = Point(x, y).scale(cell_size)

    player = Actor()
    player.set_text("#")
    player.set_font_size(font_size)
    player.set_color(Color(255,255,255))
    player.set_position(position)
'''
#manuel
#shane
import pyray

class VideoService:

    """
    Outputs the game state onto the screen.
    """

    def __init__(self, caption, width, height, cell_size, frame_rate, debug = False) -> None:

        """
        Constructs an instance of VideoService using debug mode.

        Args:
            debug (bool): whether or not to draw in debug mode.
        """

        self._caption = caption
        self._width = width
        self._height = height
        self._cell_size = cell_size
        self._frame_rate = frame_rate
        self._debug = debug

    def close_window(self):
        
        """
        Closes the window.
        """

        pyray.close_window()

    def clear_buffer(self):

        """
        Clears the buffer in preparation for the next rendering.
        NOTE! This method should be called at the beginning
        of the game's output phase.
        """

        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()

        def draw_actor(self, actor):

            """
            Draws the given actor's text on the screen.

            Args:
                actor (Actor): The actor to draw.
            """
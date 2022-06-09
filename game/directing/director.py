#cole & antonio
class Director:
    """This class directs the flow of the program. It will call various classes for funtionality.

    Attributes:
        keyboard_service: for getting directional input.
        video_service: for providing video output.
        points: (int) keeps track of points."""

    def __init__(self, keyboard_service, video_service, CELL_SIZE):
        """Constructs a new Director using the specified keyboard and video services. Initializing points for player. 

        Args:
            keyboard_service: instance of keyboard service.
            video_service: instance of video service."""
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._points = 10
        self._CELL_SIZE = CELL_SIZE

    def start_game(self, cast):
        """Starts the game using the given cast.

        Args:
            cast: the cast of actors"""
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the player.

        Args:
            cast: the cast of actors."""
        player = cast.get_first_actor("player")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)

    def _do_updates(self, cast):
        """Updates the players position and resolves any collisions with rocks and gems.

        Args:
            cast: the cast of actors."""
        banner = cast.get_first_actor("banners")
        player = cast.get_first_actor("player")
        gems = cast.get_actors("gems")
        rocks = cast.get_actors("rocks")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)

        for gem in gems:
            gem.move_down()
            if player.get_position().equals(gem.get_position()):
                message = gem.get_message()
                banner.set_text(message)
                self._points += 100
                gem.set_random_position(self._CELL_SIZE, max_x, max_y)
            elif gem.get_position().get_y() >= max_y:
                gem.set_random_position(self._CELL_SIZE, max_x, max_y)
        for rock in rocks:
            rock.move_down()
            if player.get_position().equals(rock.get_position()):
                message = rock.get_message()
                banner.set_text(message)
                self._points -= 200
                rock.set_random_position(self._CELL_SIZE, max_x, max_y)
            elif rock.get_position().get_y() >= max_y:
                rock.set_random_position(self._CELL_SIZE, max_x, max_y)

    def _do_outputs(self, cast):
        """Draws the actors on the screen.

        Args:
            cast: the cast of actors."""
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()

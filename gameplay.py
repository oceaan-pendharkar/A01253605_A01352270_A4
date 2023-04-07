import board
import character
import end_game


def game():
    game_properties = board.initialize_game(board.make_board(10, 10), character.create_character())
    board.welcome_message()
    board.enter_room(game_properties[1])
    vitals = {"alive": True, "goal achieved": False}
    while vitals["alive"] and not vitals["goal achieved"]:
        board.move_character(game_properties[0], game_properties[1])

        """Hey Martin! Just leaving a note to say that I think all of these should be part of the battle.py module.
            I've been playing the game in board.py and with the current setup (having battle chance be decided 
            when entering a room) battle is reasonably likely. """

        # if challenge:
        #     battle()
        #     check_level()
        #     if character_has_leveled():
        #         level_up()
        character.check_alive(game_properties[1])
        character.check_goal()
    end_game.endgame()


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
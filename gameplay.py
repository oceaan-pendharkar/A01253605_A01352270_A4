import board
import character


def game():
    welcome_message()
    game_properties = board.initialize_game(board.make_board(10, 10), character.create_character())
    board.enter_room(game_properties[1])
    alive = True
    goal_achieved = False
    while alive and not goal_achieved:
        board.move_character(game_properties[0], game_properties[1])
            if challenge:
                battle()
                check_level()
                if character_has_leveled():
                    level_up()
            check_alive()
            check_goal()
    endgame()


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
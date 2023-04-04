import board
import character


def game():
    welcome_message()
    game = initialize_game(board.make_board(10, 10), character.create_character())
    character = create_character()
    game_board = board.generate_board()
    enter_room(character)
    alive = True
    while alive and not goal:
        board.move_character(game[0], game[1])
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
    make_board(10, 10)


if __name__ == "__main__":
    main()
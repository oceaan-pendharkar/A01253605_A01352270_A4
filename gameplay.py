import board
import character
import end_game


def game():
    game_properties = board.initialize_game(board.make_board(10, 10), character.create_character())
    board.enter_room(game_properties[1])
    while game_properties[1]["alive"] and not game_properties[1]["goal achieved"]:
        board.move_character(game_properties[0], game_properties[1])
        board.enter_room(game_properties[1])
        character.check_vitals(game_properties[1])
    end_game.endgame(game_properties[1], game_properties[1]["alive"])


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()

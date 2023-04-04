def game():
    welcome_message()
    create_character()
    generate_board()
    enter_room()
    while alive and not goal:
        get_direction()
        validate_move()
        if valid_move:
            move_character()
            generate_room()
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
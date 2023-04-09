import random
from battle import battle_sequence

LOCATIONS = ('Some BCIT Classroom', 'Tim Hortons', "McDonald's", 'Home',
             'Granville Station', 'Waterfront Station', 'Pacific Centre',
             'Levels Nightclub', 'Nemesis Coffee', 'Kita No Donburi')


def enter_room(character: dict) -> None:
    """
    Creates a scenario for a player to engage with when they've entered a room in a game.

    :param character: the character, as a dictionary
    :precondition: description must be a string
    :precondition: character must be a dictionary
    :precondition: the constant tuple LOCATIONS must exist within the same module
    :postcondition: the player interacts with the room in a game
    :postcondition: the player's stats and points are displayed
    :postcondition: a message saying the player is leaving the room is displayed
    :raises NameError: if LOCATIONS does not exist
    """

    def generate_room() -> str:
        """
        Randomly select a room for a player to enter, in a game.

        :precondition: the constant tuple LOCATIONS must exist within the same module
        :postcondition: the room is selected for the player
        :return: the name of the room, as a string
        :raises NameError: if LOCATIONS does not exist
        """
        if character["Luck"] > 35:
            room_indices = [7, 9, 4, 5, 4, 5, 1]  # more lucky rooms than not
            selection = room_indices[random.randint(0, 6)]
        else:
            selection = random.randint(0, 9)
        return LOCATIONS[selection]

    room = generate_room()

    def complete_assignment() -> None:
        """
        Adjust a character's intelligence, frustration, and luck points to complete an assignment in a game.

        :precondition: the character must be a dictionary
        :precondition: the character must contain "Intelligence" and "Frustration" as keys, as strings
        :precondition: the values of "Intelligence" and "Frustration" in character must be integers
        """
        character["Intelligence"] += 10
        character["Luck"] -= 5

    def event_happens(description: str, chance: int, event: str) -> None:
        """
        Generate a room for a player to interact with in a game.

        :param description: the description of the room, as a string
        :param chance: the denominator of the fraction of chance an event will happen in the room, as an integer
        :param event: the event that might happen in that room
        :precondition: description must be one of the strings in LOCATIONS
        :precondition: percent must be an integer
        :precondition: event must be a string
        :precondition: attribute must be a string that exists in the character's dictionary keys
        :precondition: character must be a dictionary
        :postcondition: the player interacts with the room
        """
        print(f"You're in {description}. There is a 1/{chance} chance you will {event} if you enter one of the listed "
              f"numbers.")
        number = random.randint(1, chance)
        guess = int(input(f"Type an integer [1, {chance}]: "))
        if number == guess:
            print(f"You KNEW this would happen! You {event}.")
            if event == 'get assigned ANOTHER assignment':
                complete_assignment()
            elif event == 'have to fight':
                battle_sequence(character)
            elif event == 'gain motivation':
                character["Motivation"] += 10
            elif event == 'lose self-control':
                character["Self-Control"] -= 2
        else:
            print(f"The number was {number}.\nYou did not {event}. As you were...")

    if room == LOCATIONS[0] or room == LOCATIONS[3]:
        event_happens(room, 3, 'get assigned ANOTHER assignment')

    elif room in [LOCATIONS[1], LOCATIONS[2], LOCATIONS[8], LOCATIONS[9]]:
        event_happens(room, 2, 'have to fight')

    elif room == LOCATIONS[6] or room == LOCATIONS[7]:
        event_happens(room, 3, 'lose self-control')

    else:
        event_happens(room, 3, 'gain motivation')

    print(f"You are now leaving {room}.\nHere's what your points and stats look like:\n{character}")


def move_character(board: tuple, character: dict) -> None:
    """
    Move a character north, south, east, or west within a game board.

    :param board: the game board, as a tuple containing row and column boundaries as sub-tuples of size 2
    :param character: a dictionary
    :precondition: character must be a dictionary that contains keys "row" and "column"
    :precondition: the function enter_room must be accessible within the same module
    :postcondition: the user enters a direction 'n', 's', 'e', or 'w' to move
    :postcondition: updates the character's row or column based on the move chosen by the user
    :postcondition: calls enter_room
    :raises TypeError: if board is not a tuple
    :raises TypeError: if character is not a dict
    :raises ValueError: if the direction entered by the user is not 'n', 's', 'e', or 'w'
    :raises NameError: if enter_room does not exist within the same module
    """

    def get_user_choice() -> str:
        """
        Print a numbered list of directions and ask the user to enter the direction they wish to travel.

        :postcondition: the string prompt for user input is printed
        :postcondition: the user decides and types which direction to go next
        :return: the direction the user wishes to travel, as a string ('n', 's', 'e', or 'w')
        :raises ValueError: if direction is not 'n', 's', 'e', or 'w'
        """
        user_choice = input("Enter the direction you wish to go (n, s, e, or w): ")
        if user_choice != 'n' and user_choice != 's' and user_choice != 'w' and user_choice != 'e':
            raise ValueError
        return user_choice

    def get_row_coordinate(move: str) -> int:
        """
        Assign a new row value to a character based on the move being validated or made.

        :param move: the direction of the move, as a string 'n' or 's'
        :precondition: move must be a string of size 1, either 'n' or 's'
        :postcondition: assigns a new column value to the character based on the move
        :return: the new coordinate, as an integer
        :raises ValueError: if move is not 'n' or 's'
        """
        if move != 'n' and move != 's':
            raise ValueError("You can only use 'n' or 's' to validate or change the row coordinate")
        if move == 'n':
            return character["row"] - 1
        elif move == 's':
            return character["row"] + 1

    def get_column_coordinate(move: str) -> int:
        """
        Assign a new row value to a character based on the move being validated or made.

        :param move: the direction of the move, as a string 'e' or 'w'
        :precondition: move must be a string of size 1, either 'e' or 'w'
        :postcondition: assigns a new row value to the character based on the move
        :return: the new coordinate, as an integer
        :raises ValueError: if move is not 'e' or 'w'
        """
        if move != 'e' and move != 'w':
            raise ValueError("You can only use 'e' or 'w' to validate or change the column coordinate")
        if move == 'e':
            return character["column"] + 1
        elif move == "w":
            return character["column"] - 1

    def validate_move(bounds: tuple, move: str) -> bool:
        """
        Check that a character's move in a particular direction lands on the board of a game being played.

        :param bounds: a tuple of the board boundaries
        :param move: the direction, as a string, either 'n', 's', 'e', or 'w'
        :precondition: bounds must be a tuple
        :precondition: move must be a string, either 'n', 's', 'e', or 'w'
        :postcondition: determines whether a character's move in a particular direction lands on the playing board
        :return: True if the move falls within the board, else False
        :raises TypeError: if bounds is not a tuple
        :raises TypeError: if move is not a string
        """
        if type(bounds) != tuple or type(move) != str:
            raise ValueError("You have passed an argument of the wrong type. Please check the function documentation!")

        row, column = character["row"], character["column"]

        if move == "n" or move == "s":
            row = get_row_coordinate(move)
        elif move == 'e' or move == 'w':
            column = get_column_coordinate(move)

        if bounds[0][0] <= row < bounds[0][1] and bounds[1][0] <= column < bounds[1][1]:
            return True
        else:
            print(f"Your move must stay within the bounds of the board!")
            return False

    def keep_checking_move() -> str:
        """
        Make sure the user enters an appropriate direction, and that the direction is a valid move.

        :precondition: the user must be on the board
        :postcondition: validates the move in the chosen direction
        :postcondition: ensures that the move is only 'n', 's', 'e', or 'w'
        return: the direction of the valid move, as a string 'n', 's', 'e', or 'w'
        """
        choice_is_valid = False
        move = None
        while not choice_is_valid:
            try:
                move = get_user_choice()
            except ValueError:
                print("Direction must be 'n', 's', 'e', or 'w'!")
            else:
                choice_is_valid = validate_move(board, move)
        return move

    if type(board) != tuple or type(character) != dict:
        raise TypeError("Board must be a tuple! Character must be a dict!")

    direction = keep_checking_move()

    if direction == "n" or direction == "s":
        character["row"] = get_row_coordinate(direction)
    elif direction == 'e' or direction == 'w':
        character["column"] = get_column_coordinate(direction)

    enter_room(character)


def make_board(rows: int, columns: int) -> tuple:
    """
    Create the bounds of a board for a game, lower bound inclusive, upper bound exclusive.

    :param rows: an integer 2 or greater
    :param columns: an integer 2 or greater
    :precondition: rows must be an integer 2 or greater
    :precondition: columns must be an integer 2 or greater
    :postcondition: creates the bounds of a board for a game, lower bound inclusive, upper bound exclusive
    :return: the boundaries of the board, as a tuple with 2 sub-tuples that give the row and column bounds respectively
    :raises ValueError: if rows < 2
    :raises ValueError: if columns < 2
    >>> board = make_board(5, 5)
    >>> board
    ((0, 5), (0, 5))
    >>> board = make_board(95, 3)
    >>> board
    ((0, 95), (0, 3))
    """
    if rows < 2 or columns < 2:
        raise ValueError("Dimensions must be 2 or greater")
    boundaries = ((0, rows), (0, columns))
    return boundaries


def initialize_game(game_board: tuple, character: dict) -> tuple:
    """
    Initialize a game.

    Create a board, create a character, and print an explanatory welcome messsage.

    :param game_board: the board, as a tuple of row and column boundaries
    :param character: the character, as a dictionary
    :precondition: game_board must be a tuple with 2 sets of row/column coordinates
    :precondition: character must be a dictionary
    :precondition: character must have a "Name" key with a string as a value
    :postcondition: creates a board
    :postcondition: creates a character
    :postcondition: prints an explanatory welcome message
    :return: the board and player as two elements within a tuple
    :raises TypeError: if game_board is not a tuple
    :raises TypeError: if player is not a dict
    :raises KeyError: if "Name" does not exist as a key within character
    >>> game = initialize_game(((0, 5), (0,5)), {"Name": "Chris"})
    Welcome to the game, Chris! You are on MISSION: COMPLETE ASSIGNMENT 4.
    You're at the end of your first term in CST and things have been hectic as HECK.
    But don't worry, we know you can do it!
    Your mission is to stay Motivated enough to stay alive, achieve enough Fitness level to defeat the final boss, and
    make it to the last square of the board for the final battle...
    >>> game
    (((0, 5), (0, 5)), {'Name': 'Chris'})

    >>> game = initialize_game(((0, 7), (0, 9)), {"Name": "Newton"})
    Welcome to the game, Newton! You are on MISSION: COMPLETE ASSIGNMENT 4.
    You're at the end of your first term in CST and things have been hectic as HECK.
    But don't worry, we know you can do it!
    Your mission is to stay Motivated enough to stay alive, achieve enough Fitness level to defeat the final boss, and
    make it to the last square of the board for the final battle...
    >>> game
    (((0, 7), (0, 9)), {'Name': 'Newton'})
    """
    if type(game_board) != tuple or type(character) != dict:
        raise TypeError("Your board must be a tuple and your player must be a dictionary!")
    print(f"Welcome to the game, {character['Name']}! You are on MISSION: COMPLETE ASSIGNMENT 4.\nYou're at the end "
          f"of your first term in CST and things have been hectic as HECK.\nBut don't worry, we know you can do "
          f"it!\nYour mission is to stay Motivated enough to stay alive, achieve enough Fitness level to "
          f"defeat the final boss, and\nmake it to the last square of the board for the final battle...")
    return game_board, character


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()

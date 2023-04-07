import random
from Martn import battle

LOCATIONS = ('Some BCIT Classroom', 'Tim Hortons', "McDonald's", 'Home',
             'Granville Station', 'Waterfront Station', 'Pacific Centre',
             'Levels Nightclub', 'Nemesis Coffee', 'Kita No Donburi')


def welcome_message(character: dict) -> None:
    """
    Welcome a player to a game.

    :param character: the character, as a dictionary
    :precondition: character must be a dictionary
    :postcondition: Welcomes a player to a game
    :raises TypeError: if character is not a dictionary
    """
    if type(character) != dict:
        raise TypeError("I cannot welcome a character that is not a dictionary to this game!")

    print(f"Welcome to the game, {character['Name']}! You are on MISSION: COMPLETE ASSIGNMENT 4.\nYou're at the end "
          f"of your first term in CST and things have been hectic as HECK. But don't worry, we know you can do "
          f"it!\nYour mission is to stay Motivated enough to stay alive, achieve a high enough fitness level to "
          f"defeat the final boss, and make it to the last square of the board for the final battle...")


def enter_room(character: dict) -> None:
    """
    Creates a scenario for a player to engage with when they've entered a room in a game.

    :param character: the character, as a dictionary
    :precondition: description must be a string
    :precondition: character must be a dictionary
    :postcondition: the player interacts with the room in a game
    """

    def generate_room() -> str:
        """
        Randomly select a room for a player to enter, in a game.

        :postcondition: the room is selected for the player
        :return: the name of the room, as a string
        """
        if character["Luck"] > 75:
            room_indices = [6, 0, 7, 9, 4, 5, 8]  # more lucky rooms than not
            selection = room_indices[random.randint(0, 6)]
        else:
            selection = random.randint(0, 9)
        return LOCATIONS[selection]

    room = generate_room()

    print("You're in ", room)

    def complete_assignment() -> None:
        """
        Adjust a character's intelligence, frustration, and luck points to complete an assignment in a game.

        :precondition: the character must be a dictionary
        :precondition: the character must contain "Intelligence" and "Frustration" as keys, as strings
        :precondition: the values of "Intelligence" and "Frustration" in character must be integers
        """
        character["Intelligence"] += 10
        character["Frustration"] += 10
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
                battle(character)
            elif event == 'gain motivation':
                character["Motivation"] += 10
        else:
            print(f"The number was {number}")
            print(f"You did not {event}. As you were...")

    if room == LOCATIONS[0] or room == LOCATIONS[3]:
        event_happens(room, 3, 'get assigned ANOTHER assignment')

    elif room == LOCATIONS[1] or room == LOCATIONS[2] or room == LOCATIONS[8]:
        event_happens(room, 2, 'have to fight')

    elif room == LOCATIONS[6] or room == LOCATIONS[7] or room == LOCATIONS[9]:
        event_happens(room, 3, 'gain motivation')

    else:
        print("Nothing happens in this room. Such is life...")


def move_character(board: tuple, character: dict) -> None:
    """
    Move a character up, down, left, or right within a game board.

    :param board: the game board, as a tuple containing row and column boundaries as sub-tuples of size 2
    :param character: a dictionary
    :precondition: character must be a dictionary that contains keys "row" and "column"
    :precondition: direction must either 'n', 's', 'e', or 'w', as a string of length 1
    :precondition: the move must have been validated to make sure it is possible on the board
    :postcondition: the user enters a direction 'n', 's', 'e', or 'w' to move
    :postcondition: updates the character's row or column based on the move chosen by the user
    :raises TypeError: if board is not a tuple
    :raises TypeError: if direction is not a string
    :raises ValueError: if the direction entered by the user is not 'n', 's', 'e', or 'w'
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
        Assign a new row value based on the move being validated or made.

        :param move: the direction of the move, as a string 'n' or 's'
        :return: the new coordinate, as an integer
        :raises ValueError: if move is not 'n' or 's'
        """
        if move != 'n' and move != 's':
            raise ValueError("You can only use 'n' or 's' to validate or change the row coordinate")
        if move == 'n':
            return character["row"] - 1
        elif direction == 's':
            return character["row"] + 1

    def get_column_coordinate(move: str) -> int:
        """
        Assign a new row value based on the move being validated or made.

        :param move: the direction of the move, as a string 'e' or 'w'
        :return: the new coordinate, as an integer
        :raises ValueError: if move is not 'e' or 'w'
        """
        if move != 'e' and move != 'w':
            raise ValueError("You can only use 'e' or 'w' to validate or change the column coordinate")
        if direction == 'e':
            return character["column"] + 1
        elif direction == "w":
            return character["column"] - 1

    def validate_move() -> bool:
        """
        Check that a character's move in a particular direction lands on the board of a game being played.

        :precondition: board must be a tuple
        :precondition: direction must be a string, either 'n', 's', 'e', or 'w'
        :postcondition: determines whether a character's move in a particular direction lands on the playing board
        :return: True if the move falls within the board, else False
        :raises TypeError: if board is not a tuple
        :raises TypeError: if direction is not a string
        """
        if type(board) != tuple or type(direction) != str:
            raise ValueError("You have passed an argument of the wrong type. Please check the function documentation!")

        row, column = character["row"], character["column"]

        if direction == "n" or direction == "s":
            row = get_row_coordinate(direction)
        elif direction == 'e' or direction == 'w':
            column = get_column_coordinate(direction)

        if board[0][0] <= row < board[0][1] and board[1][0] <= column < board[1][1]:
            return True
        else:
            print(f"Your move must stay within the bounds of the board!")
            return False

    choice_is_valid = False
    direction = None
    while not choice_is_valid:
        try:
            direction = get_user_choice()
        except ValueError:
            print("Direction must be 'n', 's', 'e', or 'w'!")
        else:
            choice_is_valid = validate_move()

    if direction == "n" or direction == "s":
        character["row"] = get_row_coordinate(direction)
    elif direction == 'e' or direction == 'w':
        character["column"] = get_column_coordinate(direction)


def make_board(rows: int, columns: int) -> tuple:
    """
    Create a board for a game.

    :param rows: an integer 2 or greater
    :param columns: an integer 2 or greater
    :precondition: rows must be an integer 2 or greater
    :precondition: columns must be an integer 2 or greater
    :postcondition: creates a board for a game
    :return: the boundaries of the board, as a tuple with 2 sub-tuples that give the row and column bounds respectively
    :raises ValueError: if rows < 2
    :raises ValueError: if columns < 2
    """
    if rows < 2 or columns < 2:
        raise ValueError("Dimensions must be 2 or greater")
    boundaries = ((0, rows), (0, columns))
    return boundaries


def initialize_game(game_board: tuple, player: dict) -> tuple:
    """
    Create a board a character to engage in a game scenario.

    :param game_board: the board, as a tuple of row and column boundaries
    :param player: the character, as a dictionary
    :postcondition: creates a board and character to play a game
    :return: the board and player as two elements within a tuple
    :raises TypeError: if game_board is not a tuple
    :raises TypeError: if player is not a dict
    """
    if type(game_board) != tuple or type(player) != dict:
        raise TypeError("Your board must be a tuple and your player must be a dictionary!")
    return game_board, player


def main():
    """
    Drive the program.
    """
    bottom_row = False
    board = make_board(10, 10)
    character = {"Motivation": 20, "Frustration": 20, "Self-control": 20, "Intelligence": 20, "Luck": 20, "Speed": 20,
                 'Name': "Oceaan", 'row': 0, 'column': 0}
    while not bottom_row:
        enter_room(character)
        move_character(board, character)
        if character['row'] == 9:
            bottom_row = True
        print(character)
    print("You reached the bottom row!")


if __name__ == "__main__":
    main()

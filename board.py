import random
from Martn import battle

LOCATIONS = ('Some BCIT Classroom', 'Tim Hortons', "McDonald's", 'Home',
             'Granville Station', 'Waterfront Station', 'Pacific Centre',
             'Levels Nightclub', 'Nemesis Coffee', 'Kita No Donburi')


def event_happens(description: str, chance: int, event: str) -> bool:
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
    :return: True if the event happens, else False
    """
    print(f"You're in {description}. There is a 1/{chance} chance you will {event}.")
    number = random.randint(1, chance)
    guess = input(f"Type an integer [1, {chance}]: ")
    if number == guess:
        print(f"You KNEW this would happen! You {event}")
        return True
    else:
        print(f"You did not {event}. As you were...")
        return False


def enter_room(character: dict) -> None:
    """
    Decide which event happens to a character based on the room they've entered in a game.

    :param character: the character, as a dictionary
    :precondition: description must be a string
    :precondition: character must be a dictionary
    :postcondition: selects a particular room for a player to interact with in a game
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

    if room == LOCATIONS[0] or room == LOCATIONS[3]:
        event = event_happens(room, 3, 'get assigned ANOTHER assignment')
        if event:
            character['Frustration'] += 5

    elif room == LOCATIONS[1] or room == LOCATIONS[2] or room == LOCATIONS[8]:
        event = event_happens(room, 2, 'have to fight')
        if event:
            battle(character)

    elif room == LOCATIONS[6] or room == LOCATIONS[7] or room == LOCATIONS[9]:
        event = event_happens(room, 3, 'gain motivation')
        if event:
            character["Motivation"] += 10

    else:
        print("Nothing happens in this room. Such is life...")


def validate_move(board: tuple, character: dict, direction: str) -> bool:
    """
    Check that a character's move in a particular direction lands on the board of a game being played.

    :param board: the game board, as a tuple containing row and column boundaries as sub-tuples of size 2
    :param character: the character's row position, column position, and current stats, as a dictionary
    :param direction: either 'n', 's', 'e', or 'w' as a string
    :precondition: board must be a tuple
    :precondition: character must be a dictionary
    :precondition: direction must be a string, either 'n', 's', 'e', or 'w'
    :postcondition: determines whether a character's move in a particular direction lands on the playing board
    :return: True if the move falls within the board, else False
    :raises TypeError: if board is not a tuple
    :raises TypeError: if character is not a dict
    :raises TypeError: if direction is not a string
    :raises ValueError: if direction is not 'n', 's', 'e', or 'w'
    """
    if type(board) != tuple or type(character) != dict or type(direction) != str:
        raise ValueError("You have passed an argument of the wrong type. Please check the function documentation!")
    if direction != 'n' and direction != 's' and direction != 'w' and direction != 'e':
        raise TypeError("Direction must be 'n', 's', 'e', or 'w'!")

    bounds = board

    row = character["row"]
    column = character["column"]

    if direction == "n":
        row = character["row"] - 1
    elif direction == "s":
        row = character["row"] + 1
    elif direction == "e":
        column = character["column"] + 1
    elif direction == "w":
        column = character["column"] - 1

    if bounds[0][0] <= row <= bounds[0][1] and bounds[1][0] <= column <= bounds[1][1]:
        return True
    else:
        return False


def move_character(board: tuple, character: dict) -> None:
    """
    Move a character up, down, left, or right within a game board.

    :param board: the game board, as a tuple containing row and column boundaries as sub-tuples of size 2
    :param character: a dictionary
    :precondition: character must be a dictionary that contains keys "row" and "column"
    :precondition: direction must either 'n', 's', 'e', or 'w', as a string of length 1
    :precondition: the move must have been validated to make sure it is possible on the board
    :postcondition: updates the character's row and column
    """

    def get_user_choice() -> str:
        """
        Print a numbered list of directions and ask the user to enter the direction they wish to travel.

        :postcondition: the string prompt for user input is printed
        :postcondition: the user decides and types which direction to go next
        :return: the direction the user wishes to travel, as a string ('n', 's', 'e', or 'w')
        """
        user_choice = input("Enter the direction you wish to go (n, s, e, or w): ")
        return user_choice

    choice_is_valid = False
    while not choice_is_valid:
        direction = get_user_choice()
        choice_is_valid = validate_move(board, character, direction)

        if direction == "n":
            character["row"] -= 1
        elif direction == "s":
            character["row"] += 1
        elif direction == "e":
            character["column"] += 1
        elif direction == "w":
            character["column"] -= 1


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


def main():
    """
    Drive the program.
    """
    board = make_board(10, 10)
    character = {"Motivation": 20, "Frustration": 20, "Self-control": 20, "Intelligence": 20, "Luck": 20, "Speed": 20,
                 'Name': "Oceaan"}
    enter_room(character)
    move_character(board, character)


if __name__ == "__main__":
    main()

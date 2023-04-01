import itertools
import pprint
from Martn import luck_roll

LOCATIONS = ['Some BCIT Classroom', 'Tim Hortons', "McDonald's", 'Home',
             'Granville Station', 'Waterfront Station', 'Pacific Centre',
             'Levels Nightclub', 'Nemesis Coffee', 'Kita No Donburi']


def generate_classroom() -> None:
    """
    Generate some BCIT classroom for a player to interact with in a game.

    :postcondition: the player interacts with the room
    """
    print("You're in some BCIT classroom. There is a 10% chance you'll get assigned ANOTHER assignment.")



def select_room(description: str) -> None:
    """
    Select a specific room for a player to interact with in a game.

    :param description: a string
    :precondition: description must be a string
    :postcondition: selects a particular room for a player to interact with in a game
    """
    if description == LOCATIONS[0]:
        generate_classroom()
    elif description == LOCATIONS[1]:
        # return 10, 'gaining 10 motivation points'


def move_character(character: dict, direction: str) -> None:
    """
    Move a character up, down, left, or right within a game board.

    :param character: a dictionary
    :param direction: either 'n', 's', 'e', or 'w', as a string of length 1
    :precondition: character must be a dictionary that contains keys "row" and "column"
    :precondition: direction must either 'n', 's', 'e', or 'w', as a string of length 1
    :precondition: the move must have been validated to make sure it is possible on the board
    :postcondition: updates the character's row and column
    """
    if direction == "n":
        character["row"] -= 1
    elif direction == "s":
        character["row"] += 1
    elif direction == "e":
        character["column"] += 1
    elif direction == "w":
        character["column"] -= 1


def make_board(rows, columns):
    """
    Create a 100 X 100 board for a game.

    :param rows: an integer 2 or greater
    :param columns: an integer 2 or greater
    :precondition: rows must be an integer 2 or greater
    :precondition: columns must be an integer 2 or greater
    :postcondition: creates a board for a game
    :raises ValueError: if rows < 2
    :raises ValueError: if columns < 2
    """
    if rows < 2 or columns < 2:
        raise ValueError("Dimensions must be 2 or greater")
    room_generator = itertools.cycle(LOCATIONS)
    board = tuple([[next(room_generator) for _ in range(columns)] for _ in range(rows)])
    pprint.pprint(board, width=180)
    return board


def main():
    """
    Drive the program.
    """
    make_board(10, 10)


if __name__ == "__main__":
    main()

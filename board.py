import itertools
import pprint
import random
from Martn import battle

LOCATIONS = ['Some BCIT Classroom', 'Tim Hortons', "McDonald's", 'Home',
             'Granville Station', 'Waterfront Station', 'Pacific Centre',
             'Levels Nightclub', 'Nemesis Coffee', 'Kita No Donburi']


def generate_room(description: str, percent: int, event: str) -> bool:
    """
    Generate a room for a player to interact with in a game.

    :param description: the description of the room, as a string
    :param percent: the percent chance an event will happen in the room, as an integer
    :param event: the event that might happen in that room
    :precondition: description must be one of the strings in LOCATIONS
    :precondition: percent must be an integer
    :precondition: event must be a string
    :precondition: attribute must be a string that exists in the character's dictionary keys
    :precondition: character must be a dictionary
    :postcondition: the player interacts with the room
    :return: True if the event happens, else False
    """
    print(f"You're in {description}. There is a {percent}% chance you will {event}.")
    number = random.randint(1, percent)
    guess = input(f"Type an integer [1, {percent}]: ")
    if number == guess:
        print(f"You KNEW this would happen! You {event}")
        return True
    else:
        print(f"You did not {event}. As you were...")
        return False


def enter_room(character: dict, description: str) -> None:
    """
    Select a specific room for a player to interact with in a game.

    :param character: the character, as a dictionary
    :param description: a string, the description of the room
    :precondition: description must be a string
    :precondition: character must be a dictionary
    :postcondition: selects a particular room for a player to interact with in a game
    """
    if description == LOCATIONS[0] or description == LOCATIONS[3]:
        event_happens = generate_room(description, 10, 'get assigned ANOTHER assignment')
        if event_happens:
            character['Frustration'] += 5
    elif description == LOCATIONS[1] or description == LOCATIONS[2] or description == LOCATIONS[8]:
        event_happens = generate_room(description, 20, 'have to fight')
        if event_happens:
            battle(character)
    elif description == LOCATIONS[6] or description == LOCATIONS[7] or description == LOCATIONS[9]:
        event_happens = generate_room(description, 10, 'gain motivation')
        if event_happens:
            character["Motivation"] += 10
    else:
        print("Nothing happens in this room. Such is life...")


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

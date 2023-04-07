import itertools


def make_custom_character(character: dict) -> None:
    """
    Create a character with custom values for Motivation, Frustration, Self-Control, Intelligence, and Luck attributes.

    :character: a dictionary of attributes as strings for keys and integers for values
    :precondition: character must be a dictionary
    :precondition: character's attributes must have values of zero to start
    :postcondition: adds 120 points total to the character's attributes
    """
    points = 120
    key_generator = itertools.cycle([key for key in character.keys() if key not in ["Name", "row", "column",
                                                                                    "Fitness"]])
    while points > 0:
        key = next(key_generator)
        character[key] = int(input(f"How many points do you want to add to your {key}?"))
        points -= character[key]
        if points == 0:
            print("You've used all your points!")
            break
        elif points < 0:
            print("Woah there, that was more than 120 points!! \nSince you cheated, that's all the points you get for "
                  "now. \nAnd you can forget about getting points for the category you just over-filled. \nThat's not "
                  "how operation COMPLETE ASSIGNMENT 4 works...")
            character[key] = 0
            break
        print(f"You have {points} points left to distribute between your attributes.")


def make_preset_character(character: dict, selection: str):
    """
    Create a character with more points in one attribute, depending on the selection.

    :param character: a dictionary with attributes as strings for keys and zeroes as integers for values
    :param selection: the character type selection, as a string of length 1
    :precondition: character must be a dictionary
    :precondition: character's attributes must have zero as values to begin with
    :precondition: selection must be a string either 'n', 'l', 'g', 'j', or 'r'
    :postcondition: adds 120 points total to the character's attributes
    :raises TypeError: if selection is not a string
    :raises TypeError: if character is not a dict
    :raises TypeError: if selection is not a string
    :raises ValueError: if selection is not 'n', 'l', 'g', 'j', or 'r'
    """
    if type(character) != dict or type(selection) != str:
        raise TypeError("Character must be a dictionary! Selection must be a string!")
    if selection not in ['n', 'l', 'g', 'j', 'r']:
        raise ValueError("Character option can only be 'n', 'l', 'g', 'j', or 'r'")

    def populate_points(attribute: str) -> None:
        """
        Populate a character's points based on their selection.

        :param attribute: the attribute to give extra points, as a string, based on the user's selection
        :precondition: attribute must be a string
        :precondition: character's points must be at zero to begin with
        :precondition: character must be a dict
        :postcondition: character's points are initialized ofr game play
        :raises TypeError: if attribute is not a string
        """
        if type(attribute) != str:
            raise TypeError("The attribute you pass to populate_points must be a string!")
        key_generator = iter([attribute for attribute in character.keys() if attribute not in ["Name", "row", "column",
                                                                                               "Fitness"]])
        for _ in range(6):
            character[next(key_generator)] = 15
        character[attribute] *= 2

    if selection == 'r':
        for key in [key for key in character.keys() if key not in ["Name", "row", "column", "Fitness"]]:
            character[key] = 20
    elif selection == 'n':
        populate_points('Intelligence')
    elif selection == 'l':
        populate_points('Luck')
    elif selection == 'g':
        populate_points('Self-Control')
    elif selection == 'j':
        populate_points('Speed')


def create_character() -> dict:
    """
    Create a character.

    :postcondition: creates a character, as a dictionary of attributes as keys and integer values
    :return: the character, as a dictionary
    """
    character = {"Motivation": 0, "Frustration": 0, "Self-control": 0, "Intelligence": 0, "Luck": 0, "Speed": 0,
                 "Fitness": 0, 'Name': input("What's your character's name? "), "row": 0, "column": 0}
    choice = input("Would you like to choose how many points to put in each category? y/n ")

    if choice == 'y':
        print(f"Alright! You have ***120 points*** to distribute between Motivation, Frustration, Self-Control, "
              "Intelligence, Luck, and Speed.\nMotivation: helps you stay alive\nFrustration: you want to keep this "
              "low during battle!\nSelf-Control: like defense\nIntelligence: helps you damage your enemies\nLuck: "
              "determines how likely you are to meet difficult opponents\nSpeed: helps you be quicker than your "
              "enemies!\nYou also have Fitness, which keeps track of your experience level (0 for now!).")
        make_custom_character(character)

    else:
        character_type = input(f"That's cool, we have a few preset categories. Type the first letter of the character "
                               "type to select it.\nnerd: has a lot of intelligence, obviously(n)\nleprechaun: has a "
                               "lot of luck, obviously(l)\ngreat ape: has a lot of self control (maybe not obvious) (g)"
                               "\njock: has a lot of speed\nregular person: has an even distribution of points(r) ")
        make_preset_character(character, character_type)

    return character


def check_alive(character: dict) -> None:
    """
    Check to see if a character's motivation has dropped to or below zero in a game.

    :param character: the character, as a dictionary
    :precondition: character must be a dictionary
    :return: True if alive, else False
    :raises TypeError: if character is not a dictionary
    """
    if type(character) != dict:
        raise TypeError("Character must be a dictionary to call check_alive!")

    if character["Motivation"] < 0:
        return True
    else:
        return False


def check_goal(character: dict) -> None:
    """
    Check that a character has a high enough fitness level and

    :param character:
    :return:
    """
def main():
    """
    Drive the program.
    """
    character = create_character()
    print(character)


if __name__ == "__main__":
    main()

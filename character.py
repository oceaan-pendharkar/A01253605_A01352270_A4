import itertools


def make_custom_character(character: dict) -> None:
    """
    Create a character with custom values for Motivation, Frustration, Self-Control, Intelligence, and Luck attributes.

    :character: a dictionary of attributes as strings for keys and integers for values
    :precondition: character must be a dictionary
    :precondition: character's attributes must have values of zero to start
    :postcondition: adds 120 points total to the character's attributes
    """
    points = 30
    print(points)
    key_generator = itertools.cycle([key for key in character.keys() if key not in ["Name", "row", "column",
                                                                                    "Fitness", "Level", "alive",
                                                                                    "goal achieved"]])
    while points > 0:
        print(points)
        key = next(key_generator)
        point_increase = int(input(f"How many points do you want to add to your {key}?"))
        character[key] += point_increase
        points -= point_increase
        if points == 0:
            print("You've used all your points!")
            break
        elif points < 0:
            print(f"Woah there, that was more than {points} points!! \nSince you cheated, that's all the points you "
                  "get for now. \nAnd you can forget about getting points for the category you just over-filled. "
                  "\nThat's not how operation COMPLETE ASSIGNMENT 4 works...")
            character[key] -= point_increase
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
                                                                                               "Fitness", "Level",
                                                                                               "alive",
                                                                                               "goal achieved"]])
        for _ in range(6):
            character[next(key_generator)] = 15
        character[attribute] *= 2

    if selection == 'r':
        for key in [key for key in character.keys() if key not in ["Name", "row", "column", "Fitness", "Level",
                                                                   "alive", "goal achieved"]]:
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
    character = {"Motivation": 70, "Max Frustration": 50, "Self-Control": 5, "Intelligence": 5, "Luck": 5, "Speed": 5,
                 "Fitness": 5, 'Name': input("What's your character's name? "), "row": 0, "column": 0, "Level": 1,
                 "alive": True, "goal achieved": False}
    choice = input("Would you like to choose how many points to put in each category? y/n ")

    if choice == 'y':
        print(f"Alright! Here are your base stats:\n{character}\nYou have ***30 points*** to distribute between "
              "Motivation, Max Frustration, Self-Control, Intelligence, Luck, and Speed.\nMotivation: helps you stay "
              "alive\nMax Frustration: the higher this is, the longer you last in battle\nSelf-Control: like defense"
              "\nIntelligence: helps you damage your enemies\nLuck: determines how likely you are to meet difficult "
              "opponents\nSpeed: helps you be quicker than your enemies!\nYou also have Fitness, which keeps track "
              "of your experience level (0 for now!).")
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
    :postcondition: updates character's "alive" attribute to False if their motivation has dropped to zero or below
    :raises TypeError: if character is not a dictionary
    """
    if type(character) != dict:
        raise TypeError("Character must be a dictionary to call check_alive!")

    if character["Motivation"] < 0:
        character["alive"] = False


def check_goal(character: dict) -> None:
    """
    Check that a character has a high enough fitness level and has reached the correct square to defeat the boss.

    :param character: a dictionary
    :precondition: character must be a dictionary
    :postcondition: displays the character's progress towards their goal if their fitness level is 30 or higher or
                    if they've found the final square
    :postcondition: updates "goal achieved" attribute of character if Fitness >= 30 and coordinates = (9, 9)
    :raises TypeError: if character is not a dictionary
    """
    if type(character) != dict:
        raise TypeError("Character must be a dictionary to call check_goal!")

    character_coordinates = (character["row"], character["column"])

    if character["Fitness"] >= 30 and character_coordinates == (9, 9):
        print(f"Nice job, {character['Name']}. You've reached the final square and you're ready to defeat the final "
              f"boss!!!")
        character["goal achieved"] = True
    elif character["Fitness"] >= 30 and character_coordinates != (9, 9):
        print(f"Alright, {character['Name']}. You've got enough fitness points to defeat the final boss! Make your "
              f"way to the final square for the final battle...")
    elif character["Fitness"] < 30 and character_coordinates == (9, 9):
        print(f"Hey there, {character['Name']}, you've found the final square, but you aren't ready to defeat the "
              f"boss yet! Keep trucking...")


def check_vitals(character: dict) -> None:
    """
    Check if a character is alive and whether they have achieved their goal

    :param character: a dictionary
    :return: True if character is still in the game, else False
    """
    check_alive(character)
    check_goal(character)


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()

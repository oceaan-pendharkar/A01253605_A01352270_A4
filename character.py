import itertools


def populate_custom_points(character: dict, points) -> None:
    """
    Add points to a selection of attributes of a character based on user input.

    :character: a dictionary of attributes as strings for keys and integers for values
    :precondition: character must be a dictionary
    :precondition: character's attributes must have values of zero to start
    :postcondition: adds 120 points total to the character's attributes
    """
    key_generator = itertools.cycle([key for key in character.keys() if key not in ["Name", "row", "column",
                                                                                    "Fitness", "Level", "alive",
                                                                                    "goal achieved"]])
    while points > 0:
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


def make_preset_character(character: dict) -> None:
    """
    Give 10 extra points to a character in one attribute, depending on the selection.

    :param character: a dictionary with attributes as strings for keys and integers for values
    :precondition: character must be a dictionary
    :precondition: character's attributes must have zero as values to begin with
    :postcondition: adds 120 points total to the character's attributes
    :postcondition: the user selects 'n', 'l', 'g', or 'j' (otherwise will loop forever)
    :postcondition: the character's attribute is given 10 points based on the user's selection
    :raises TypeError: if character is not a dict
    """
    if type(character) != dict:
        raise TypeError("Character must be a dictionary! Selection must be a string!")
    selection = None
    while selection not in ['n', 'l', 'g', 'j']:
        selection = input(f"That's cool, we have a few preset categories. Type the first letter of the "
                          f"character type to select it.\nnerd: has a lot of intelligence, obviously(n)\n"
                          f"leprechaun: has a lot of luck, obviously(l)\ngreat ape: has a lot of self control "
                          f"(maybe not obvious) (g)\njock: has a lot of speed")
        if selection == 'n':
            character["Intelligence"] += 10
        elif selection == 'l':
            character["Luck"] += 10
        elif selection == 'g':
            character["Self-Control"] += 10
        elif selection == 'j':
            character["Speed"] += 10
        else:
            print("You must enter 'n', 'l', 'g', or 'j'. Try again...")


def create_character() -> dict:
    """
    Create a character.

    :postcondition: creates a character, as a dictionary of attributes as keys and integer values
    :return: the character, as a dictionary
    """
    character = {"Motivation": 10, "Max Frustration": 60, "Self-Control": 5, "Intelligence": 5, "Luck": 5, "Speed": 5,
                 "Fitness": 5, 'Name': input("What's your character's name? "), "row": 0, "column": 0, "Level": 1,
                 "alive": True, "goal achieved": False}
    choice = None
    while choice != 'y' and choice != 'n':
        choice = input("Would you like to choose the categories to which you want to distribute your 10 points? y/n ")
        if choice == 'y':
            print(f"Alright! Here are your base stats:\n{character}\nYou have ***10 points*** to distribute between "
                  "Motivation, Max Frustration, Self-Control, Intelligence, Luck, and Speed.\nMotivation: helps you "
                  "stay alive\nMax Frustration: the higher this is, the longer you last in battle\nSelf-Control: like "
                  "defense\nIntelligence: helps you damage your enemies\nLuck: determines how likely you are to meet "
                  "difficult opponents\nSpeed: helps you be quicker than your enemies!\nYou also have Fitness, which "
                  "keeps track of your experience level (0 for now!).")
            populate_custom_points(character, 10)

        elif choice == 'n':
            make_preset_character(character)
        else:
            print("You entered something other than 'y' or 'n'. Try again...")
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
    me = create_character()
    print(me)


if __name__ == "__main__":
    main()

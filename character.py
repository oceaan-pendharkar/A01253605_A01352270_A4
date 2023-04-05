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
    new_character = character
    key_generator = itertools.cycle(list(["Motivation", "Frustration", "Self-control", "Intelligence", "Luck",
                                          "Speed"]))
    while points > 0:
        key = next(key_generator)
        character[key] = int(input(f"How many points do you want to add to your {key}?"))
        points -= new_character[key]
        if points == 0:
            print("You've used all your points!")
            break
        elif points < 0:
            print("Woah there, that was more than 120 points!! \nSince you cheated, that's all the points you get for "
                  "now. \nAnd you can forget about the extra ones you tried to give yourself. \nThat's not how "
                  "operation COMPLETE ASSIGNMENT 4 works...")
            new_character[key] = 0
            break
        print(f"You have {points} points left to distribute between your attributes.")


def populate_points(character: dict, selection: str) -> dict:
    """
    Create a character with a lot of intelligence points.

    :param character: a dictionary with attributes as strings for keys and zeroes as integers for values
    :param selection: the character type, as a string of length 1
    :precondition: character must be a dictionary
    :precondition: character's attributes must have zero as values to begin with
    :postcondition: adds 120 points total to the character's attributes
    """
    for key in character.keys():
        character[key] = 15
    if selection == 'n':
        character['Intelligence'] += 25
    elif selection == 'l':
        character['Luck'] += 25
    elif selection == 'g':
        character['Self-control'] += 25
    elif selection == 'j':
        character['Speed'] += 25
    elif selection == 'r':
        for key in character.keys():
            character[key] += 5


def create_character() -> dict:
    """
    Create a character.

    :postcondition: creates a character, as a dictionary of attributes as keys and integer values
    :return: the character, as a dictionary
    """
    character = {"Motivation": 0, "Frustration": 0, "Self-control": 0, "Intelligence": 0, "Luck": 0, "Speed": 0,
                 'Name': input("What's your character's name? ")}
    choice = input("Would you like to choose how many points to put in each category? y/n")

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
                               "\njock: has a lot of speed\nregular person: has an even distribution of points(r)")
        populate_points(character, character_type)

    character['Fitness'] = 0
    return character


def main():
    """
    Drive the program.
    """
    character = create_character()
    print(character)


if __name__ == "__main__":
    main()

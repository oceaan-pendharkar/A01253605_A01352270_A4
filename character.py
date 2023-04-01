def make_custom_character(character: dict) -> None:
    """
    Create a character with custom values for Motivation, Frustration, Self-Control, Intelligence, and Luck attributes.

    :character: a dictionary of attributes as strings for keys and integers for values
    :precondition: character must be a dictionary
    :precondition: character's attributes must have values of zero to start
    :postcondition: adds 100 points total to the character's attributes
    """
    points = 100
    new_character = character
    for key in new_character.keys():
        character[key] = int(input(f"How many points do you want to add to your {key}?"))
        points -= new_character[key]
        if points == 0:
            print("You've used all your points!")
            break
        elif points < 0:
            print("Woah there, that was more than 100 points!! \nSince you cheated, that's all the points you get for "
                  "now. \nAnd you can forget about the extra ones you tried to give yourself. \nThat's not how "
                  "operation COMPLETE ASSIGNMENT 4 works...")
            new_character[key] = 0
            break


def populate_points(character: dict, selection: str) -> dict:
    """
    Create a character with a lot of intelligence points.

    :param character: a dictionary with attributes as strings for keys and zeroes as integers for values
    :param selection: the character type, as a string of length 1
    :precondition: character must be a dictionary
    :precondition: character's attributes must have zero as values to begin with
    :postcondition: adds 100 points total to the character's attributes
    """
    for key in character.keys():
        character[key] = 15
    if selection == 'n':
        character['intelligence'] += 25
    elif selection == 'l':
        character['luck'] += 25
    elif selection == 'g':
        character['self-control'] += 25
    elif selection == 'r':
        for key in character.keys():
            character[key] += 5


def create_character() -> dict:
    """
    Create a character.

    :postcondition: creates a character, as a dictionary of attributes as keys and integer values
    :return: the character, as a dictionary
    """
    character = {"motivation": 0, "frustration": 0, "self-control": 0, "intelligence": 0, "luck": 0,
                 'name': input("What's your character's name?")}
    choice = input("Would you like to choose how many points to put in each category? y/n")

    if choice == 'y':
        print("Alright! You have ***100 points*** to distribute between Motivation, Frustration, Self-Control, "
              "Intelligence, and Luck.\nMotivation: helps you stay alive\nFrustration: you want to keep this low during"
              "battle!\nSelf-Control: like defense\nIntelligence: helps you damage your enemies\nLuck: determines how "
              "likely you are to meet difficult opponents\nYou also have Fitness, which keeps track of your "
              "experience level (0 for now!).")
        make_custom_character(character)

    else:
        character_type = input("That's cool, we have a few preset categories. Type the first letter of the character "
                               "type to select it.\nnerd: has a lot of intelligence, obviously(n)\nleprechaun: has a "
                               "lot of luck, obviously(l)\ngreat ape: has a lot of self control (maybe not obvious) (g)"
                               "\nregular person: has an even distribution of points(r)")
        populate_points(character, character_type)

    character['fitness'] = 0
    return character


def main():
    """
    Drive the program.
    """
    character = create_character()
    print(character)


if __name__ == "__main__":
    main()

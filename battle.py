import random


def determine_enemy():
    """
    Select enemy from list of enemies.

    :postcondition: randomly selects and returns an enemy from a dictionary of preset enemy dictionaries
    :return: the randomly selected enemy dictionary
    """
    enemies = {1: {'Name': 'Tim Hortons', 'Description': 'You are at Tim Hortons and there is a muffin that you want.',
                   'Frustration': 15, 'Intelligence': 7, 'Speed': 2, "Self-Control": 2, 'Max_Frustration': 20, "Exp": 2},
               2: {'Name': "McDonald's", 'Description': "You are at Mcdonald's", 'Frustration': 12, 'Intelligence': 8,
                   'Speed': 5, "Self-Control": 2, 'Max_Frustration': 20, "Exp": 1}}

    selector = random.randint(1, len(enemies))
    enemy = enemies[selector]
    print(enemies[selector]['Description'])
    return enemy


def luck_roll(luck, lower, upper, luck_multiplier=0):
    """
    Determine the number of a roll with luck modifiers.

    Randomly generates a number for a roll and adds on luck modifiers to the roll.

    :param luck: an integer
    :param lower: another integer
    :param upper: another integer
    :param luck_multiplier: a float number, default is 0
    :precondition: luck must be an integer
    :precondition: lower must be an integer
    :precondition: upper must be an integer
    :precondition: luck_multiplier must a float
    :precondition: if no argument is passed for luck_multiplier, default value is 0
    :postcondition: generates and returns a number that is randomly between lower and upper inclusive and
                    adds a luck multiplier to the number
    :return: the random number as an int
    """
    roll = round(random.randint(lower, upper) + luck * luck_multiplier)
    return roll


def check_first(character, enemy):
    character_speed = character['Speed'] + luck_roll(character['Luck'], -2, 2, 0.3)
    enemy_speed = enemy['Speed'] + luck_roll(0, -2, 2)
    if character_speed >= enemy_speed:
        print("You have higher speed and attack first")
        return True
    else:
        print(f"{enemy['Name']} has higher speed and attacks first")
        return False


def calculate_critical(luck):
    base_crit_chance = 5
    random_number = random.randint(1, 100)
    critical = base_crit_chance + luck_roll(luck, 0, 0, 0.3)
    if random_number <= critical:
        return True
    else:
        return False


def deal_damage(character_is_faster, character, enemy):
    if character_is_faster:
        character_critical = calculate_critical(character["Luck"])
        if character_critical:
            character_damage = character["Intelligence"] * 1.5
            print("You landed a critical hit!")
        else:
            character_damage = character['Intelligence'] - enemy["Self-Control"]
        enemy['Frustration'] += character_damage
        print(f"You frustrated {enemy['Name']} by {character_damage} points")
    else:
        enemy_critical = calculate_critical(0)
        if enemy_critical:
            enemy_damage = enemy['Intelligence'] * 1.5
            print(f"Oh no! {enemy['Name']} landed a critical hit on you!")
        else:
            enemy_damage = enemy['Intelligence'] - character["Self-Control"]
        character['Frustration'] += enemy_damage
        print(f"{enemy['Name']} frustrated you by {enemy_damage} points")


def calculate_fitness(character, enemy):
    character["Fitness"] += enemy["Exp"]
    print(f"You've gained {enemy['Exp']} fitness points from defeating {enemy['Name']}")
    if character["Fitness"] >= 15 and character["Level"] < 2:
        character["Level"] = 2
        print("Congratulations! You have reached level 2!")
    elif character["Fitness"] >= 30 and character["Level"] < 3:
        character["Level"] = 3
        print("Congratulations! You've reached level 3! Go get that boss now.")
    else:
        pass


def battle_loss(character, enemy):
    print(f"You gave in to the temptation of {enemy['Name']}! You lost 20 motivation.")
    character["Motivation"] -= 20


def battle_win(character, enemy):
    print("You won the battle!")
    calculate_fitness(character, enemy)


def check_result(character, enemy, lose_function, win_function):
    if character['Frustration'] >= character["Max_Frustration"]:
        lose_function(character, enemy)
    else:
        win_function(character, enemy)


def battle(character_is_faster, character, enemy, enemy_frustration):
    while character['Frustration'] < character["Max_Frustration"] and enemy['Frustration'] < enemy_frustration:
        deal_damage(character_is_faster, character, enemy)
        if character['Frustration'] < character["Max_Frustration"] and enemy['Frustration'] < enemy_frustration:
            deal_damage(not character_is_faster, character, enemy)


def battle_sequence(character):
    enemy = determine_enemy()
    character["Frustration"] = 0
    character_is_faster = check_first(character, enemy)
    battle(character_is_faster, character, enemy, enemy["Max_Frustration"])
    check_result(character, enemy, battle_loss, battle_win)


def main():
    """
    Drive the program.
    """
    character = {'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 3, 'Luck': 5,
                 "Self-Control": 4, "Level": 1, "Fitness": 14, "Max_Frustration": 10}
    battle_sequence(character)


if __name__ == '__main__':
    main()

import random
import copy
from character import populate_custom_points


def determine_enemy(character):
    """
    Select enemy from list of enemies.

    :postcondition: randomly selects and returns a copy of enemy from a dictionary of preset enemy dictionaries
    :return: a copy of the randomly selected enemy dictionary
    """
    enemies = {1: {'Name': 'Chicken Sandwich', 'Description': 'On the table lies a delicious chicken sandwich. The '
                                                              'crisp, juicy, and tender chicken strips lie between 2 '
                                                              'slices of freshly baked bread. You can feel the '
                                                              'growling in our stomach drawing you towards it...',
                   'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 21, 'Speed': 5, "Self-Control": 3,
                   "Luck": 0, "Exp": 1},
               2: {'Name': 'Donut', 'Description': 'You can see a donut on display by the front counter. The glaze '
                                                   'on top of the donut glistens in the light, tempting you towards '
                                                   'its sweetness.',
                   'Frustration': 0, 'Max Frustration': 11, 'Intelligence': 19, 'Speed': 3, "Self-Control": 7,
                   "Luck": 0, "Exp": 2},
               3: {'Name': 'Latte', 'Description': 'Looking at the menu, you dream about holding a warm latte in your '
                                                   'hands. The scent of the tea and milk fills your mind and you can'
                                                   'almost taste the contrast of the smooth milky foam and the '
                                                   'green tea under it. Will you end up ordering it?',
                   'Frustration': 0, 'Max Frustration': 14, 'Intelligence': 24, 'Speed': 11, "Self-Control": 1,
                   "Luck": 0, "Exp": 1},
               4: {'Name': 'Breakfast Sandwich', 'Description': 'You see someone eating a warm breakfast sandwich '
                                                                'through the window. The perfectly cooked egg, crispy'
                                                                'bacon and melted cheese beckon you towards the store.',
                   'Frustration': 0, 'Max Frustration': 25, 'Intelligence': 15, 'Speed': 4, "Self-Control": 3,
                   "Luck": 0, "Exp": 2},
               5: {'Name': 'Hashbrowns', 'Description': 'The thought of hashbrowns fill your mind. From the satisfying '
                                                        'crunch of the potatoes to the savory flavors of the potatoes'
                                                        'your body craves for a rest to indulge in this fried '
                                                        'delicacy.',
                   'Frustration': 0, 'Max Frustration': 20, 'Intelligence': 20, 'Speed': 4, "Self-Control": 3,
                   "Luck": 0, "Exp": 2},
               6: {'Name': 'Soft Drink', 'Description': 'A cold soft drink sits on the counter here. The fizzing of '
                                                        'the bubble reaches your ears, inviting you to partake in the '
                                                        'sweet beverage. You resist its temptation as you try to pop'
                                                        'your cravings.',
                   'Frustration': 0, 'Max Frustration': 18, 'Intelligence': 20, 'Speed': 6, "Self-Control": 2,
                   "Luck": 0, "Exp": 2},
               7: {'Name': 'Muffin', 'Description': 'The aroma of freshly baked muffins hits you. You think of the '
                                                    'golden brown exterior of the muffin, and its soft fruity interior.'
                                                    'You wonder if you should sit down and enjoy this breakfast treat.',
                   'Frustration': 0, 'Max Frustration': 16, 'Intelligence': 19, 'Speed': 4, "Self-Control": 5,
                   "Luck": 0, "Exp": 2},
               8: {'Name': 'Ice Cream', 'Description': 'As you watch someone eat their delicious ice cream cone, you '
                                                       'imagine the smooth, creamy texture of it. The sweet milky'
                                                       'flavor of the ice cream mixed with whatever flavor you desire. '
                                                       'Vanilla, chocolate, and oreo, it could all be yours...',
                   'Frustration': 0, 'Max Frustration': 20, 'Intelligence': 21, 'Speed': 6, "Self-Control": 4,
                   "Luck": 0, "Exp": 2}}

    selector = random.randint(1, len(enemies))
    enemy = copy.deepcopy(enemies[selector])
    for key, value in enemy.items():
        if key not in ["Name", "Description", "Frustration", "Exp"]:
            increased_stat = value * (1 + character["Level"] * 0.1)
            enemy[key] = round(increased_stat)
    print(enemies[selector]['Description'])
    return enemy


def luck_roll(luck, lower, upper, luck_multiplier=0):
    """
    Determine the number of a roll with luck modifiers.

    Randomly generates a number for a roll and adds on luck modifiers to the roll.

    :param luck: an integer
    :param lower: another integer
    :param upper: another integer
    :param luck_multiplier: a number, default is 0
    :precondition: luck must be an integer
    :precondition: lower must be an integer
    :precondition: upper must be an integer
    :precondition: luck_multiplier must a number, either a float or an int
    :precondition: if no argument is passed for luck_multiplier, default value is 0
    :postcondition: generates and returns a number that is randomly between lower and upper inclusive and
                    adds a luck multiplier to the number
    :return: the random number as an int
    """
    if type(luck) is not int:
        raise TypeError("Luck stat needs to be an integer!")
    if type(lower) is not int:
        raise TypeError("Lower bound needs to be an integer!")
    if type(upper) is not int:
        raise TypeError("Upper bound needs to be an integer!")
    if type(luck_multiplier) is not float and type(luck_multiplier) is not int:
        raise TypeError("Luck multiplier must be a number!")
    roll = round(random.randint(lower, upper) + luck * luck_multiplier)
    return roll


def check_first(character, enemy):
    """
    Check if the character is faster or enemy is faster.

    :param character: a dictionary describing the character's stats
    :param enemy: a dictionary describing the enemy's stats
    :precondition: character must be a dictionary
    :precondition: character must have at least 2 keys named 'Speed' and 'Luck'
    :precondition: enemy must be a dictionary
    :precondition: enemy must have at least 2 keys named 'Speed' and 'Name'
    :postcondition: compare speed of character and enemy and return True if character is faster and False if enemy is
    :postcondition: print a statement informing user who goes first depending on if character is faster or not
    :return: True if character is faster and False if enemy is faster
    :raises TypeError: if character is not a dictionary
    :raises TypeError: if enemy is not a dictionary
    :raises KeyError: if 'Speed' key or 'Luck' key is not in character
    :raises KeyError: if 'Speed' key or 'Name' key is not in enemy
    """
    if type(character) is not dict or type(enemy) is not dict:
        raise TypeError("Character and Enemy must be dictionaries!")
    if 'Speed' not in character or 'Luck' not in character:
        raise KeyError("Character must have speed and luck stats!")
    if 'Speed' not in enemy or 'Name' not in enemy:
        raise KeyError("Enemy must have speed stat and a name")
    character_speed = character['Speed'] + luck_roll(character['Luck'], -2, 2, 0.3)
    enemy_speed = enemy['Speed'] + luck_roll(0, -2, 2)
    if character_speed >= enemy_speed:
        print("You have higher speed and attack first")
        return True
    else:
        print(f"{enemy['Name']} has higher speed and attacks first")
        return False


def deal_damage(character_is_faster, character, enemy):
    def calculate_critical(luck):
        base_crit_chance = 5
        random_number = random.randint(1, 100)
        critical = base_crit_chance + luck_roll(luck, 0, 0, 0.3)
        if random_number <= critical:
            return True
        else:
            return False

    def calculate_damage(attacker, defender):
        attacker_critical = calculate_critical(attacker["Luck"])
        if attacker_critical:
            attacker_damage = attacker["Intelligence"] * 1.5
            print(f"{attacker['Name']} landed a critical hit!")
        else:
            attacker_damage = attacker['Intelligence'] - defender["Self-Control"]

        return validate_damage(attacker_damage)

    def validate_damage(damage):
        if damage <= 0:
            damage = 1
            return damage
        else:
            return damage

    if character_is_faster:
        character_damage = calculate_damage(character, enemy)
        enemy['Frustration'] += character_damage
        print(f"You frustrated {enemy['Name']} by {character_damage} points")
    else:
        enemy_damage = calculate_damage(enemy, character)
        character['Frustration'] += enemy_damage
        print(f"{enemy['Name']} frustrated you by {enemy_damage} points")


def level_up(character):
    points = 10
    print(f"You have {points} to allocate to your stats. Possible stats to increase are Motivation, Max Frustration,"
          "Self-Control, Intelligence, Luck, and Speed. Please allocate your points. ")
    populate_custom_points(character, 10)


def calculate_fitness(character, enemy):
    character["Fitness"] += enemy["Exp"]
    print(f"You've gained {enemy['Exp']} fitness points from defeating {enemy['Name']}")
    if character["Fitness"] >= 15 and character["Level"] < 2:
        character["Level"] = 2
        print("Congratulations! You have reached level 2!")
        level_up(character)
    elif character["Fitness"] >= 30 and character["Level"] < 3:
        character["Level"] = 3
        print("Congratulations! You've reached level 3! Go get that boss now.")
        level_up(character)
    else:
        pass


def battle_loss(character, enemy):
    print(f"You gave in to the temptation of {enemy['Name']}! You lost 20 motivation.")
    character["Motivation"] -= 20


def battle_win(character, enemy):
    print("You won the battle!")
    calculate_fitness(character, enemy)


def check_result(character, enemy, lose_function, win_function):
    if character['Frustration'] >= character["Max Frustration"]:
        lose_function(character, enemy)
    else:
        win_function(character, enemy)


def battle(character_is_faster, character, enemy, enemy_frustration):
    while character['Frustration'] < character["Max Frustration"] and enemy['Frustration'] < enemy_frustration:
        deal_damage(character_is_faster, character, enemy)
        if character['Frustration'] < character["Max Frustration"] and enemy['Frustration'] < enemy_frustration:
            deal_damage(not character_is_faster, character, enemy)


def battle_sequence(character):
    enemy = determine_enemy(character)
    character["Frustration"] = 0
    character_is_faster = check_first(character, enemy)
    battle(character_is_faster, character, enemy, enemy["Max Frustration"])
    check_result(character, enemy, battle_loss, battle_win)


def main():
    """
    Drive the program.
    """
    character = {'Motivation': 100, 'Frustration': 0, 'Intelligence': 10, 'Speed': 3, 'Luck': 5,
                 "Self-Control": 4, "Level": 1, "Fitness": 14, "Max Frustration": 10}
    battle_sequence(character)


if __name__ == '__main__':
    main()

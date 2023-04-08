import random


def determine_enemy():
    enemies = {1: {'Name': 'Tim Hortons', 'Description': 'You are at Tim Hortons and there is a muffin that you want.',
                   'Frustration': 15, 'Intelligence': 7, 'Speed': 2, 'Max_Frustration': 20, "Exp": 2},
               2: {'Name': "McDonald's", 'Description': "You are at Mcdonald's", 'Frustration': 12, 'Intelligence': 8,
                   'Speed': 5, 'Max_Frustration': 20, "Exp": 1}}

    selector = random.randint(1, len(enemies))
    enemy = enemies[selector]
    print(enemies[selector]['Description'])
    return enemy


def luck_roll(luck, lower, upper, luck_multiplier=0):
    roll = random.randint(lower, upper) + luck * luck_multiplier
    return roll


def check_first(character, enemy):
    character_speed = character['Speed'] + luck_roll(character['Luck'], -2, 2, 0.3)
    enemy_speed = enemy['Speed'] + luck_roll(0, -2, 2)
    if character_speed >= enemy_speed:
        return True
    else:
        return False


def deal_damage(character_is_faster, character, enemy):
    character_damage = (character['Intelligence'] + luck_roll(0, -2, 2))
    enemy_damage = (enemy['Intelligence'] + luck_roll(0, -2, 2))

    if character_is_faster:
        enemy['Frustration'] += character_damage
    else:
        character['Frustration'] += enemy_damage


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


def check_result(character, exp):
    if character['Frustration'] >= character["Max_Frustration"]:
        print("Sorry you lost the battle! You've lost 20 motivation from giving into the temptation")
        character["Motivation"] -= 20
    else:
        print("You won the battle!")
        calculate_fitness(character, exp)


def battle(character_is_faster, character, enemy, enemy_frustration):
    while character['Frustration'] < character["Max_Frustration"] and enemy['Frustration'] < enemy_frustration:
        deal_damage(character_is_faster, character, enemy)
        if character['Frustration'] < character["Max_Frustration"] and enemy['Frustration'] < enemy_frustration:
            deal_damage(not character_is_faster, character, enemy)
            print(character)


def battle_sequence(character):
    enemy = determine_enemy()
    character_is_faster = check_first(character, enemy)
    battle(character_is_faster, character, enemy, enemy["Max_Frustration"])
    check_result(character, enemy)


def main():
    """
    Drive the program.
    """
    character = {'Motivation': 100, 'Frustration': 1, 'Intelligence': 10, 'Speed': 3, 'Luck': 5, "Level": 1,
                 "Fitness": 14, "Max_Frustration": 2}
    battle_sequence(character)


if __name__ == '__main__':
    main()

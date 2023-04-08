import random


def determine_enemy():
    enemies = {1: {'Name': 'Tim Hortons', 'Description': 'You are at Tim Hortons and there is a muffin that you want.',
                   'Frustration': 15, 'Intelligence': 7, 'Speed': 2, "Exp": 2},
               2: {'Name': "McDonald's", 'Description': "You are at Mcdonald's", 'Frustration': 12, 'Intelligence': 8,
                   'Speed': 5, "Exp": 1}}

    selector = random.randint(1, len(enemies))
    enemy = enemies[selector]
    print(enemies[selector]['Description'])
    return enemy


def luck_roll(luck, lower, upper, luck_multiplier=0):
    roll = random.randint(lower, upper) + luck * luck_multiplier
    return roll


def check_first(character, enemy):
    if character['Speed'] + luck_roll(character['Luck'], 1, 3, 0.3) >= enemy['Speed'] + luck_roll(0, -2, 2):
        return True
    if character['Speed'] + luck_roll(character['Luck'], 1, 3, 0.3) < enemy['Speed'] + luck_roll(0, -2, 2):
        return False


def deal_damage(character_is_faster, character, enemy):
    if character_is_faster:
        enemy['Frustration'] -= character['Intelligence'] + luck_roll(0, -2, 2)
    if not character_is_faster:
        character['Frustration'] -= enemy['Intelligence'] + luck_roll(0, -2, 2)


def check_result(character):
    if character['Frustration'] <= 0:
        print("Sorry you lost the battle!")
    else:
        print("You won the battle!")


def battle(character_is_faster, character, enemy, enemy_frustration):
    while character['Frustration'] <= 0 or enemy['Frustration'] <= enemy_frustration:
        deal_damage(character_is_faster, character, enemy)
        if character['Frustration'] > 0 or enemy['Frustration'] > enemy_frustration:
            deal_damage(not character_is_faster, character, enemy)


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


def battle_sequence(character):
    enemy = determine_enemy()
    character_is_faster = check_first(character, enemy)
    battle(character_is_faster, character, enemy, 0)
    check_result(character)
    calculate_fitness(character, enemy)


def main():
    """
    Drive the program.
    """
    character = {'Motivation': 100, 'Frustration': 75, 'Intelligence': 10, 'Speed': 8, 'Luck': 5, "Level": 1,
                 "Fitness": 14}
    battle_sequence(character)


if __name__ == '__main__':
    main()

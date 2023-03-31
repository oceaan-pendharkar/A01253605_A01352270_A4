import random


def determine_enemy():
    enemies = {1: {'Name': 'Tim Hortons', 'Description': 'You are at Tim Hortons and there is a muffin that you want.',
                   'Frustration': 15, 'Intelligence': 7, 'Speed': 2},
               2: {'Name': "McDonald's", 'Description': "You are at Mcdonald's", 'Frustration': 12, 'Intelligence': 8,
                   'Speed': 5}}

    selector = random.randint(1, len(enemies))
    enemy = enemies[selector]
    print(enemies[selector]['Description'])
    return enemy


def luck_roll(luck, lower, upper, luck_multiplier=0):
    roll = random.randint(lower, upper) + luck * luck_multiplier
    return roll


def check_first(character, enemy):
    if character['speed'] + luck_roll(character['luck'], 1, 3, 0.3) >= enemy['speed'] + luck_roll(0, 1, 3):
        return [character, enemy]
    if character['speed'] + luck_roll(character['luck'], 1, 3, 0.3) < enemy['speed'] + luck_roll(0, 1, 3):
        return [enemy, character]


def battle(character):
    enemy = determine_enemy()
    # first_to_strike = check_first(character, enemy)
    # while character['Frustration'] is not 0 or enemy['Frustration'] is not 0:
        # deal_damage(first_to_strike)
        # is_alive()
        # deal_damage(slower, faster)
        # is_alive()


def main():
    """
    Drive the program.
    """
    character = {'Motivation': 100, 'Frustration': 75, 'Intelligence': 10, 'Speed': 8, 'luck': 5}
    battle(character)


if __name__ == '__main__':
    main()

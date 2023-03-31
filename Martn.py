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
    if character['Speed'] + luck_roll(character['Luck'], 1, 3, 0.3) >= enemy['Speed'] + luck_roll(0, 1, 3):
        return True
    if character['Speed'] + luck_roll(character['Luck'], 1, 3, 0.3) < enemy['Speed'] + luck_roll(0, 1, 3):
        return False


def deal_damage(character_is_faster, character, enemy):
    if character_is_faster:
        enemy['Frustration'] -= character['Intelligence']
    if not character_is_faster:
        character['Frustration'] -= enemy['Intelligence']


def battle(character):
    enemy = determine_enemy()
    character_is_faster = check_first(character, enemy)
    # while character['Frustration'] <= 0 or enemy['Frustration'] <= 0:
    deal_damage(character_is_faster, character, enemy)
    print(character)
    print(enemy)
        # is_alive()
        # deal_damage(first_to_strike.reverse())
        # is_alive()


def main():
    """
    Drive the program.
    """
    character = {'Motivation': 100, 'Frustration': 75, 'Intelligence': 10, 'Speed': 8, 'Luck': 5}
    battle(character)


if __name__ == '__main__':
    main()

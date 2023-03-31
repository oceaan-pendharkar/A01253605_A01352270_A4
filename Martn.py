import random


def determine_enemy():
    enemies = {1: {'Name': 'Tim Hortons', 'Description': 'You are at Tim Hortons and there is a muffin that you want.',
                   'HP': 10, 'Damage': 7, 'Speed': 2}, 2: {'Name': "McDonald's", 'Description': "You are at Mcdonald's",
                                                           'HP': 5, 'Damage': 8, 'Speed': 5}}

    selector = random.randint(1, len(enemies))
    print(enemies[selector]['Description'])


def main():
    """
    Drive the program.
    """
    determine_enemy()
    # battle()


if __name__ == '__main__':
    main()

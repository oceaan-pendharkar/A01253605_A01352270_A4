def is_alive(character):
    if character["Motivation"] <= 0:
        return False
    else:
        return True


def endgame(character):
    alive = is_alive(character)
    print(alive)
    # if alive:
    #     boss_fight()
    # else:
    #     death()


def main():
    """
    Drive the program.
    """
    character = {'Motivation': 100, 'Frustration': 75, 'Intelligence': 10, 'Speed': 8, 'Luck': 5}
    endgame(character)


if __name__ == '__main__':
    main()

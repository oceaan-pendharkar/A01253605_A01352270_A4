import battle


def is_alive(character):
    if character["Motivation"] <= 0:
        return False
    else:
        return True


def mid_boss_event(character, boss):
    print("An annoying event is happening!")
    boss["Intelligence"] *= 1.5
    boss["Speed"] *= 1.5
    character["Frustration"] += 50


def boss_fight(character):
    boss = {"Name": "Big Bad Boss", "Frustration": 0, "Max_Frustration": 1000, "Intelligence": 69, "Speed": 69}
    character_is_faster = battle.check_first(character, boss)
    battle.battle(character_is_faster, character, boss, boss["Max_Frustration"] / 2)
    if character["Frustration"] < character["Max_Frustration"]:
        mid_boss_event(character, boss)
    battle.battle(character_is_faster, character, boss, boss["Max_Frustration"])
    check_result()


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
    character = {'Motivation': 100, 'Frustration': 0, "Max_Frustration": 500, 'Intelligence': 100,
                 'Speed': 85, 'Luck': 45}
    endgame(character)


if __name__ == '__main__':
    main()

import battle


def is_alive(character):
    if character["Motivation"] <= 0:
        return False
    else:
        return True


def mid_boss_event(character, boss):
    print("You've finished making all the code for assignment 1! You bask in your achievement before a sinking "
          "realization dawns upon you. You still have to unit test everything... The thought of the endless unit tests"
          "makes you more frustrated and makes Assignment 4 so much harder to complete. Assignment 4's stats have"
          "increased and your frustration increases by 50.")
    boss["Intelligence"] *= 1.5
    boss["Speed"] *= 1.5
    character["Frustration"] += 50


def go_for_a_walk(character):
    character["row"] += battle.luck_roll(0, -2, 2)
    character["column"] += battle.luck_roll(0, -2, 2)


def boss_lose(character, enemy):
    print(f"{enemy['Name']} has frustrated you so much, that you just gave up. You lost 30 motivation. You decided to "
          f"go for a walk and ended up near the school")
    character["Motivation"] -= 30
    go_for_a_walk(character)


def boss_win(character, enemy):
    print(f"Congratulations! You've beaten {enemy['Name']} and have completed the game!")


def boss_fight(character):
    boss = {"Name": "Assignment 1", "Frustration": 0, "Max_Frustration": 1000, "Intelligence": 69, "Speed": 69, "Self-Control": 69}
    character_is_faster = battle.check_first(character, boss)
    battle.battle(character_is_faster, character, boss, boss["Max_Frustration"] / 2)
    if character["Frustration"] < character["Max_Frustration"]:
        mid_boss_event(character, boss)
    battle.battle(character_is_faster, character, boss, boss["Max_Frustration"])
    battle.check_result(character, boss, boss_lose, boss_win)


def endgame(character):
    alive = is_alive(character)
    print(alive)
    if alive:
        boss_fight(character)
    else:
        print("You lost all your motivation to finish assignment 4 and you decided that it's not worth it. It's such "
              "a nice day out right now you might as well go and enjoy life. Like a normal person...")


def main():
    """
    Drive the program.
    """
    character = {'Motivation': 100, 'Frustration': 0, "Max_Frustration": 500, 'Intelligence': 100,
                 'Speed': 85, "Self-Control": 5, 'Luck': 45, "row": 85, "column": 85}
    endgame(character)


if __name__ == '__main__':
    main()

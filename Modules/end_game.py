"""
Oceaan Pendharkar A01253605
Martin Siu A01352270
"""
import Modules.battle


def mid_boss_event(character, boss):
    print("You've finished making all the code for assignment 1! You bask in your achievement before a sinking "
          "realization dawns upon you. You still have to unit test everything... The thought of the endless unit tests"
          "makes you more frustrated and makes Assignment 4 so much harder to complete. Assignment 4's stats have"
          "increased and your frustration increases by 50.")
    boss["Intelligence"] = round(boss["Intelligence"] * 1.1)
    boss["Speed"] *= round(boss["Speed"] * 1.1)
    character["Frustration"] += 10


def boss_lose(character, enemy):
    print(f"{enemy['Name']} has frustrated you so much, that you just gave up. You decided that life is too short to "
          f"be working all the time, and you need to enjoy life.")


def boss_win(character, enemy):
    print(f"Congratulations! You've beaten {enemy['Name']} and have completed the game! Hopefully your instructor will"
          f" give you a good mark for it? Please?")


def boss_fight(character):
    boss = {"Name": "Assignment 4", "Frustration": 0, "Max Frustration": 200, "Intelligence": 25, "Speed": 30,
            "Self-Control": 15, "Luck": 0, 'Exp': 0}
    character_is_faster = Modules.battle.check_first(character, boss)
    Modules.battle.battle(character_is_faster, character, boss, boss["Max Frustration"] / 2)
    if character["Frustration"] < character["Max Frustration"]:
        mid_boss_event(character, boss)
    Modules.battle.battle(character_is_faster, character, boss, boss["Max Frustration"])
    Modules.battle.check_result(character, boss, boss_lose, boss_win)


def endgame(character, alive):
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
    character = {'Name': 'Bob', 'Motivation': 100, 'Frustration': 0, "Max Frustration": 500, 'Intelligence': 100,
                 'Speed': 85, "Self-Control": 5, 'Level': 3, 'Fitness': 30, 'Luck': 45, "row": 85, "column": 85}
    endgame(character, True)


if __name__ == '__main__':
    main()

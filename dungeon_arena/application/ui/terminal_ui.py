DRAGON_ART = r"""
                 / \  //\
  |\___/|      /   \//  \\
  /0  0  \__  /    //  | \ \
 /     /  \/_/    //   |  \  \
 @_^_@'/   \/_   //    |   \   \
 //_^_/     \/_ //     |    \    \
( //) |        \///      |     \     \
( / /) _|_ /   )  //       |      \     _\
( // /) '/,_ _ _/  ( ; -.    |    _ _\.-~        .-~~~^-.
(( / / )) ,-{        _      `-.|.-~-.           .~         `.
(( // / ))  '/\      /                 ~-. _ .-~      .-~^-.  \
(( /// ))      `.   {            }                   /      \  \
 (( / ))     .----~-.\        \-'                 .~         \  `. \^-.
            ///.----..>        \             _ -~             `.  ^-`  ^-_
              ///-._ _ _ _ _ _ _}^ - - - - ~                     ~-- ,.-~
"""


def progress_bar(current: int, maximum: int, width: int = 24) -> str:
    filled = round(width * current / maximum) if maximum else 0
    filled = max(0, min(width, filled))
    return f"[{'#' * filled}{'-' * (width - filled)}] {current}/{maximum}"


def show_title() -> None:
    print("\n" + "=" * 58)
    print("                 D U N G E O N   A R E N A")
    print("=" * 58)
    print(DRAGON_ART)
    print("A wild Dragon appears!")


def show_status(dragon_health: int, player_mana: int) -> None:
    print("\n🐉 Dragon  " + progress_bar(dragon_health, 50))
    print("✨ Mana    " + progress_bar(player_mana, 10))


def show_weapon_menu() -> None:
    print("\nChoose your weapon:")
    print("  1. ⚔️  Sword       Reliable physical damage")
    print("  2. 🏹 Bow         Stronger from long range")
    print("  3. 🔮 Magic Staff Powerful, but costs mana")
    print("  4. 🪓 Ancient Axe  Heavy physical damage")
    print("  q. 🏃 Flee")

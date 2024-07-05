import os
import time
import msvcrt

def apply_mod(game_globals):
    def you_dead(cause=None):
        game_globals['clear_terminal']()
        max_width = 40
        you_dead_str = "YOU DEAD"

        while True:
            for i in range(max_width - len(you_dead_str)):
                game_globals['clear_terminal']()
                print("#" * max_width)
                print(f"{' ' * i}{you_dead_str}")
                print("#" * max_width)
                print("\nDo you want to restart? (y/n)")

                choice = game_globals['input_with_timeout'](0.1)
                if choice == "y":
                    game_globals['restart_current_level']()
                    return
                elif choice == "n":
                    exit()
            for i in range(max_width - len(you_dead_str), 0, -1):
                game_globals['clear_terminal']()
                print("#" * max_width)
                print(f"{' ' * i}{you_dead_str}")
                print("#" * max_width)
                print("\nDo you want to restart? (y/n)")

                choice = game_globals['input_with_timeout'](0.1)
                if choice == "y":
                    game_globals['restart_current_level']()
                    return
                elif choice == "n":
                    exit()

    def input_with_timeout(timeout):
        start_time = time.time()
        while True:
            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8').lower()
                if key in ["y", "n"]:
                    return key
            if time.time() - start_time > timeout:
                return None

    def restart_current_level():
        game_globals['player_health'] = 100
        game_globals['main_game_loop']()

    game_globals['you_dead'] = you_dead
    game_globals['input_with_timeout'] = input_with_timeout
    game_globals['restart_current_level'] = restart_current_level


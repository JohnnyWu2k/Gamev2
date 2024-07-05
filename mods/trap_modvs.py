import os
import time
import pygame

# 初始化音效
pygame.mixer.init()
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sounds_dir = os.path.join(parent_dir, 'sounds')

def apply_mod(game_globals):
    def handle_interaction(y, x):
        cell = game_globals['maps'][game_globals['current_level']][y][x]
        if cell == "*":  # 如果碰到陷阱
            game_globals['player_health'] -= 50
            play_sound(os.path.join(game_globals['sounds_dir'], "explosion.wav"))
            if game_globals['player_health'] <= 0:
                play_sound(os.path.join(game_globals['sounds_dir'], "defeat.wav"))
                print("You were defeated by a trap!")
                time.sleep(1)
                game_globals['you_dead']("trap")
            else:
                print("You stepped on a hidden trap!")
                time.sleep(1)
                game_globals['update_map'](y, x, " ")  # 将陷阱移除

        # 调用原始的 handle_interaction
        return original_handle_interaction(y, x)

    def play_sound(sound_file):
        try:
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
        except pygame.error as e:
            print(f"Error playing sound: {e}")

    # 替换原始 handle_interaction
    original_handle_interaction = game_globals['handle_interaction']
    game_globals['handle_interaction'] = handle_interaction

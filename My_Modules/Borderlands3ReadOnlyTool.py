import ctypes.wintypes
import os
import re
# import stat

CSIDL_PERSONAL = 5      # My Documents
SHGFP_TYPE_CURRENT = 1  # Get current, not default value

buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)

borderlands_3_save_path = os.path.normpath(os.path.join(buf.value, "my games/Borderlands 3/Saved/SaveGames/76561198110445082"))

game_files = [f for f in os.listdir(borderlands_3_save_path) if os.path.isfile(os.path.join(borderlands_3_save_path, f))]
game_saves = [f for f in game_files if(re.match(r"^\S*(.sav)$", f) and (re.match(r"^((?!profile).)*$", f)))]

if __name__ == '__main__':
    for f in game_saves:
        print(f)

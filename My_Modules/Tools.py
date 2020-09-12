import ctypes.wintypes
import os
import re
# import stat


class Borderlands3ReadOnlyTool:

    game_saves = ""

    def __init__(self):
        csidl_personal = 5  # My Documents
        shgfp_type_current = 1  # Get current, not default value

        buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, csidl_personal, None, shgfp_type_current, buf)

        borderlands_3_save_path = os.path.normpath(os.path.join(buf.value, "my games/Borderlands 3/Saved/SaveGames/76561198110445082"))
        game_files = [f for f in os.listdir(borderlands_3_save_path) if os.path.isfile(os.path.join(borderlands_3_save_path, f))]
        self.game_saves = [f for f in game_files if(re.match(r"^\S*(.sav)$", f) and (re.match(r"^((?!profile).)*$", f)))]

    def get_saves(self):
        return self.game_saves


if __name__ == '__main__':
    test = Borderlands3ReadOnlyTool()
    print(test.get_saves())

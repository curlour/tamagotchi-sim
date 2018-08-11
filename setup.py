import cx_Freeze
import pyperclip
import sys

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"

executables = [cx_Freeze.Executable("Tamagotchi_PC.py", base = base, icon = 'Sprites/Misc/icon/icon.ico')]

cx_Freeze.setup(
    name = "Eternitchi",
    options = {"build_exe" : {"packages" : ["pygame", "dbm", "pyperclip"], "include_files" : ['Backgrounds/',
                                                                                 'Sound/',
                                                                                 'Sprites/',
                                                                                 'CCharacters/',
                                                                                 'CFood/',
                                                                                 'Inbox/',
                                                                                 'Borders/',
                                                                                 'Kitchen/',
                                                                                 'WC/',
                                                                                 'Bathroom/',
                                                                                 'ConCode/',
                                                                                 'save.txt',
                                                                                 'libogg.dll',
                                                                                 'libvorbis.dll',
                                                                                 'libvorbisfile.dll']}},
    version = "1.0.0",
    description = "Tamagotchi simulator",
    author = "curlour",
    executables = executables,
    )

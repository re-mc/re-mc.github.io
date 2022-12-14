"""
Minecraft mod installer
"""

from atools import *

wget = aImport('wget')

menu_text = "Test Menu:\n A: Set Minecraft Folder\n B: Test Program\n C: Test Download\n D: Install Mod\n E: Remove All Mods\n('exit' to quit) "

minecraft_dir = "%appdata%\\.minecraft"

def set_folder():
    minecraft_dir = input("Enter your .minecraft path (default is %appdata%\\.minecraft )\n ")


def test():
    print("Test")

def test_download():
    wget.download("https://github.com/re-mc/re-mc.github.io/raw/main/testfolder/test.py")

def autoinstall(modurl):
    modname = wget.download(modurl)
    os.system(f'move "{modname}" {minecraft_dir}\\mods\\')

def download_mod():
    url = input("Enter the URL of the mod:\n ")
    autoinstall(url)

def download_file():
    url = input("Enter the URL of the mod:\n ")
    wget.download(modurl)


def remove_mods():
    os.system(f"remove {minecraft_dir}\\mods\\*")

functions = {
    'a': set_folder,
    'b': test,
    'c': test_download,
    'd': download_mod,
    'e': remove_mods
}

menu = Menu(functions, menu_text, use_inputmsg = True)

menu.loop()

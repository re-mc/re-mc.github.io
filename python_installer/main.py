# yes

from atools import *

wget = aImport('wget')

menu_text = "Test Menu:\n A: Test Program\n B: Test Download\n C: Install Mod\n('exit' to quit) "

def test():
    print("Test")

def test_download():
    wget.download("https://github.com/re-mc/re-mc.github.io/raw/main/testfolder/test.py")

def autoinstall(modurl):
    modname = wget.download(modurl)
    os.system(f'copy "{modname}" %appdata%\\.minecraft\\mods\\')

def download_mod():
    url = input("Enter the URL of the mod: ")
    autoinstall(url)

functions = {
    'a': test,
    'b': test_download,
    'c': download_mod
}

menu = Menu(functions, menu_text, use_inputmsg = True)

menu.loop()

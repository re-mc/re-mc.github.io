# yes

from atools import *

wget = aImport('wget')

menu_text = "Test Menu:\n A: Test Program\n B: Test Download\n('exit' to quit) "

def test():
    print("Test")

def test_download():
    wget.download("https://github.com/re-mc/re-mc.github.io/raw/main/testfolder/test.py")

functions = {
    'a': test,
    'b': test_download
}

menu = Menu(functions, menu_text, use_inputmsg = True)

menu.loop()

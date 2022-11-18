import atools

menu_text = "Test Menu:\n A: Test Program\n('exit' to quit) "

def test():
    print("Test")

functions = {
    'a': test
}

menu = Menu(functions, menu_text, use_inputmsg = True)

menu.loop()
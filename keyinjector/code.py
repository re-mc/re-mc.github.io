from time import sleep
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

led.value = True
waitTime = 5
while waitTime > 0:
    waitTime -= 1
    sleep(0.5)
    led.value = True
    sleep(0.5)
    led.value = False

sleep(2)

led.value = True

keycodes = {          'A': Keycode.A,
                      'B': Keycode.B,
                      'C': Keycode.C,
                      'D': Keycode.D,
                      'E': Keycode.E,
                      'F': Keycode.F,
                      'G': Keycode.G,
                      'H': Keycode.H,
                      'I': Keycode.I,
                      'J': Keycode.J,
                      'K': Keycode.K,
                      'L': Keycode.L,
                      'M': Keycode.M,
                      'N': Keycode.N,
                      'O': Keycode.O,
                      'P': Keycode.P,
                      'Q': Keycode.Q,
                      'R': Keycode.R,
                      'S': Keycode.S,
                      'T': Keycode.T,
                      'U': Keycode.U,
                      'V': Keycode.V,
                      'W': Keycode.W,
                      'X': Keycode.X,
                      'Y': Keycode.Y,
                      'Z': Keycode.Z,
                      '1': Keycode.ONE,
                      '2': Keycode.TWO,
                      '3': Keycode.THREE,
                      '4': Keycode.FOUR,
                      '5': Keycode.FIVE,
                      '6': Keycode.SIX,
                      '7': Keycode.SEVEN,
                      '8': Keycode.EIGHT,
                      '9': Keycode.NINE,
                      '0': Keycode.ZERO,
                      'ENTER': Keycode.ENTER,
                      'RETURN': Keycode.RETURN,
                      'ESCAPE': Keycode.ESCAPE,
                      'BACKSPACE': Keycode.BACKSPACE,
                      'TAB': Keycode.TAB,
                      'SPACE': Keycode.SPACEBAR,
                      '^':     Keycode.SPACEBAR,
                      '-': Keycode.MINUS,
                      '=': Keycode.EQUALS,
                      '(': Keycode.LEFT_BRACKET,
                      ')': Keycode.RIGHT_BRACKET,
                      '\\': Keycode.BACKSLASH,
                      '#': Keycode.POUND,
                      ';': Keycode.SEMICOLON,
                      "'": Keycode.QUOTE,
                      '`': Keycode.GRAVE_ACCENT,
                      ',': Keycode.COMMA,
                      '.': Keycode.PERIOD,
                      'n.': Keycode.PERIOD,
                      '/': Keycode.FORWARD_SLASH,
                      'CAPS_LOCK': Keycode.CAPS_LOCK,
                      'F1': Keycode.F1,
                      'F2': Keycode.F2,
                      'F3': Keycode.F3,
                      'F4': Keycode.F4,
                      'F5': Keycode.F5,
                      'F6': Keycode.F6,
                      'F7': Keycode.F7,
                      'F8': Keycode.F8,
                      'F9': Keycode.F9,
                      'F10': Keycode.F10,
                      'F11': Keycode.F11,
                      'F12': Keycode.F12,
                      'PS': Keycode.PRINT_SCREEN,
                      'SCROLL_LOCK': Keycode.SCROLL_LOCK,
                      'PAUSE': Keycode.PAUSE,
                      'INSERT': Keycode.INSERT,
                      'HOME': Keycode.HOME,
                      'PAGE_UP': Keycode.PAGE_UP,
                      'DELETE': Keycode.DELETE,
                      'END': Keycode.END,
                      'PAGE_DOWN': Keycode.PAGE_DOWN,
                      'RIGHT': Keycode.RIGHT_ARROW,
                      'LEFT': Keycode.LEFT_ARROW,
                      'DOWN': Keycode.DOWN_ARROW,
                      'n*': Keycode.KEYPAD_ASTERISK,
                      'n+': Keycode.KEYPAD_PLUS,
                      'CONTROL': Keycode.CONTROL,
                      'SHIFT': Keycode.SHIFT,
                      'ALT': Keycode.ALT,
                      'OPTION': Keycode.OPTION,
                      'META': Keycode.GUI,
                      'WINDOWS': Keycode.WINDOWS,
                      'COMMAND': Keycode.COMMAND,
                      'RIGHT_CONTROL': Keycode.RIGHT_CONTROL,
                      'RIGHT_SHIFT': Keycode.RIGHT_SHIFT,
                      'RIGHT_ALT': Keycode.RIGHT_ALT,
                      'UP': Keycode.UP_ARROW,
                      'NUMLOCK': Keycode.KEYPAD_NUMLOCK,
                      'MENU': Keycode.APPLICATION,
                      'POWER': Keycode.POWER
                      }


Script = open('config.txt', 'r').read()

with open(Script, 'r') as keyfile:
    keystr = str(keyfile.read())
    keys = list(keystr.split('\n'))
    mode = ''
    for num in range(len(keys)-1):
        if keys[num] == '':
            keys.pop(num)
    for i in range(3):
        if keys[i] == '#clicking':
            mode = 'click'
        elif keys[i] == '#typing':
            print(keys)
            for string in keys:
                strsplit = string.split(' ')
                if strsplit[0] == 'type':
                    typestring = strsplit[1].upper()
                    for key in typestring:
                        try:
                            keyboard.press(keycodes[key])
                            sleep(0.05)
                            keyboard.release(keycodes[key])
                        except:
                            print('Unknown Keycode')
                elif strsplit[0] == 'delay':
                    sleep(int(strsplit[1])*0.1)
                elif strsplit[0] == 'press':
                    keyboard.press(keycodes[strsplit[1]])
                elif strsplit[0] == 'release':
                    keyboard.release(keycodes[strsplit[1]])
                elif strsplit[0] == '#':
                    None
                else:
                    for key in strsplit:
                        if mode == 'click':
                            try:
                                keyboard.press(keycodes[key])
                                sleep(0.05)
                                keyboard.release(keycodes[key])
                            except:
                                print('Unknown Keycode')
            led.value = False
            quit()
        else:
            keys.pop(i)
            mode = 'click'
    print(keys)
    for key in keys:
        if mode == 'click':
            try:
                keyboard.press(keycodes[key])
                sleep(0.05)
                keyboard.release(keycodes[key])
            except:
                print('Unknown Keycode')
                    
led.value = False












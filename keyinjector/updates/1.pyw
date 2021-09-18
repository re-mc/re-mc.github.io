#Update 1: Copy First Use Files
import sys
import os
import getpass

statusfile = open('installstatus.txt', 'r')
statusfile.write('working')

if sys.platform == 'linux':
    #Install Updating File For Later Use By User
    os.system(f'mkdir /media/{getpass.getuser()}/CIRUITPY/Update')
    os.system('wget re-mc.github.io/keyinjector/1/Update/linux.txt')
    os.system(f'mv linux.txt /media/{getpass.getuser()}/CIRUITPY/Update/linux.txt')
    os.system('wget re-mc.github.io/keyinjector/1/Update/windows.txt')
    os.system(f'mv linux.txt /media/{getpass.getuser()}/CIRUITPY/Update/windows.txt')
    #Install helloworld Demo Script
    os.system('wget re-mc.github.io/keyinjector/1/helloworld.txt')
    os.system(f'mv helloworld.txt /media/{getpass.getuser()}/CIRUITPY/helloworld.txt')
    #Install nothing Script And Set In Config
    os.system('wget re-mc.github.io/keyinjector/1/nothing.txt')
    os.system(f'mv nothing.txt /media/{getpass.getuser()}/CIRUITPY/nothing.txt')
    with open(f'/media/{getpass.getuser()}/CIRUITPY/config.txt', 'w') as configfile:
        configfile.write('nothing.txt')

statusfile.write('done')
statusfile.close()
#picoupdater part of keyinjector project
import sys
import os
import getpass
from time import sleep
from urllib import request

try:
    updateversion = sys.argv[1]
except:
    updateversion = 'latest'
if sys.platform == 'linux':
    ver_file = open(f'/media/{getpass.getuser()}/CIRCUITPY/version.txt', 'rw')
    version = ver_file.read()
    while version < int(request.urlopen('re-mc.github.io/keyinjector/version.txt')):
        os.system(f'wget re-mc.github.io/keyinjector/updates/{version+1}.pyw')
        os.system(f'python3 {version+1}.pyw &')
        while open('installstatus.txt', 'r').read() != 'done':
            sleep(0.1)
        version += 1
        ver_file.write(str(version))

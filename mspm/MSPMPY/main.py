import sys

mode = 'none'

try:
    argument = sys.argv[1]
except:
    print('Unable to fetch arguments, using dual as mode')
    mode = 'dual'
    argument = 'failed'

if argument == 'failed':

    if sys.argv[1] == 'html':
        mode = 'html'
    elif sys.argv[1] == 'local':
        mode = 'local'
    else:
        mode = 'dual'


def html():
    print('using html as mode')

def local():
    print('using local as mode')

def dual():
    print('using dual mode as none was stated')


if mode == 'html':
    html()

if mode == 'local':
    local()

if mode == 'dual':
    dual()


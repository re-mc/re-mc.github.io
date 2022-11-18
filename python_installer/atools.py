"""
AitherNight's Tools
Version 0.4.2
"""

try:
    from write_lib import color # Needed for colors, turn off colors in config to not require this file
except ModuleNotFoundError:
    class Color:
        reset = ''
        def __getitem__(*args):
            return ''
    color = Color()

config = {
    'version': '0.4.2',
    'debug': False,
    'standalone': True,
    'logname': 'LOG',
    'inputmsg': 'Press [ENTER] To Continue',
    'need_restart': False,
    'colors': True
}




modules = [
    'math'
]

module = {}


def log(text: str, end: str = '\n'):
    if config['debug']:
        if config['colors']:
            print(f'{color["yellow"]}[{config["logname"]}]: {text}{color.reset}', end=end)
        else:
            print(f'[{config["logname"]}]: {text}', end=end)



class colors:
    if config['colors']:
        reset = color.reset
        warning = color['red']
        logtext = color['yellow']
        notice = color['green']
    else:
        warning = ''
        logtext = ''
        notice = ''
        reset = ''

class Compile:
    modules_loaded = False
    def coreModules(self): # Define Core Modules -------------------------------
        self.os = __import__('os')
        self.sys = __import__('sys')
        self.json = __import__('json')
        log('imported core modules;')
        self.modules_loaded = True
        return (self.os, self.sys, self.json)
    def jsonFiles(self):
        global modules
        if self.modules_loaded:
            #if 'config.json' in self.os.listdir('atools'):
            try:
                j_config = self.json.load(open('atools/config.json', 'r'))
            except:
                try:
                    j_config = self.json.load(open('config.json', 'r'))
                except:
                    print(f'{colors.warning}!!! JSON SETTINGS NOT LOADED, DEFAULTING TO STANDALONE SETTINGS !!!{colors.reset}')
                    config['standalone'] = True
            if 'silence' not in j_config.keys():
                silence = j_config['silence']
            else:
                silence = False
            if j_config['version'] != config['version']:
                print(f"{colors.warning}! CONFIG VERSIONS DON'T MATCH !{colors.reset}")
            for i in j_config.keys():
                config[i] = j_config[i]
            config['standalone'] = False
            log('json config loaded;')
            
            try:
                modules = self.json.load(open('atools/modules.json', 'r'))
            except:
                modules = self.json.load(open('modules.json', 'r'))
            
        else:
            print('!!! JSON SETTINGS NOT LOADED, DEFAULTING TO STANDALONE SETTINGS !!!')
            config['standalone'] = True
            

def inputmsg():
    input(config['inputmsg'])

def aImport(mod: str, *contents):
    if mod in module:
        if len(contents) > 0:
            mod_content = module[mod].__dict__
            if len(contents) == 1:
                return mod_content[contents[0]]
            output = []
            for i in contents:
                output.append(mod_content[i])
            return tuple(output)
        else:
            return module[mod]
    else:
        print(f'{colors.warning}Module [{mod}] Not Loaded; Aborting;{colors.reset}')
        exit()

class Menu:
    def __init__(self, functions: dict, menu_text: str, exit_keywords: list = None, use_inputmsg: bool = False):
        if exit_keywords == None:
            exit_keywords = ['stop', 'exit', 'quit', 'abort', 'q']
        self.exit_keywords = exit_keywords
        self.functions = functions
        self.menu_text = menu_text
        self.use_inputmsg = use_inputmsg
    def open(self):
        self.answer = input(self.menu_text).lower()
        if self.answer in self.functions.keys():
            function = self.functions[self.answer]
            clear()
            function()
        if self.use_inputmsg and self.answer not in self.exit_keywords:
            inputmsg()
    def loop(self):
        self.answer = ''
        while self.answer not in self.exit_keywords:
            clear()
            self.open()

class cmdline:
    def __init__(self, args):
        args.pop(0)
        self.args = args
        self.options = {}
    def __add__(self, other: tuple):
        text, function = other
        self.options[text] = function
    def run(self):
        for i in self.args:
            if i in self.options.keys():
                function = self.options[i]
                function()
    def __sub__(self, other):
        args = self.args
        for i in args:
            if i[0] == '-':
                args.remove(i)
        


if __name__ == 'atools':
    log('Importing Core Modules;')
    compiler = Compile()
    os, sys, json = compiler.coreModules() # Init Core Modules -----------------
    if not config['standalone']:
        log('Loading JSON Config;')
        compiler.jsonFiles()
    log('Importing All Modules;')
    log(sys.platform)
    if sys.platform in ['windows', 'win32']:
        config['nt'] = True
        exec = f'"{sys.executable}"'
    else:
        config['nt'] = False
        exec = 'python3'
    config['win'] = config['nt']
    for i in modules:
        try:
            module[i] = __import__(i)
            log(f'module [{i}] imported;', end=' ')
        except ModuleNotFoundError:
            log(f'module [{i}] not imported; installing [{i}];', end=' ')
            error = os.system(f'{exec} -m pip install {i}')
            error2 = os.system(f'{exec} -m pip3 install {i}')
            if error > 0 and error2 > 0:
                print(f'{colors.warning}\n!! While starting atools module [{i}] might not have been installed correctly !!{colors.reset}')
            else:
                log(f'module [{i}] installed successfully;', end=' ')
            config['need_restart'] = True
    log(f'atools: version {config["version"]}; Initialized;')


def version():
    print(f"{colors.notice}ATools Version {config['version']}{colors.reset}")

if __name__ == '__main__':
    config['debug'] = False
    compiler = Compile()
    os, sys, json = compiler.coreModules()  # Init Core Modules

    cmd = cmdline(sys.argv)
    cmd + ('--version', version)
    cmd.run()



def clear(starting_text: str = ''):
    print(starting_text, end='')
    if config['nt']:
        os.system('cls')
    else:
        os.system('clear')

def pip(action: str):
    if config['nt']:
        os.system(f'{exec} -m pip {action}')
    else:
        os.system(f'{exec} -m pip3 {action}')

#this file contains defs, needed for PyXi bot

import vars, os

def test():
    print('Hello, world')

def version():
    print(vars.version)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def PyXi_do(command):
    if command == 'test':
        test()
    elif command == 'ver':
        version()
    elif command == 'cls':
        cls()
    else:
        print(f'{command} not defined')
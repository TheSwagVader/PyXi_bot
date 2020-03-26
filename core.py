#this is PyXi bot core

import variables

from interpret import PyXi_do

current = variables.none_root_name
root = False
if variables.default_cls:
    PyXi_do('cls')
if variables.launch_as_root:
    root = True
print(f'PyXi bot ver. {variables.version}')
while True:
    if root:
        com = input(f'{variables.base_name}>{variables.root_name}>')
    else:
        com = input(f'{variables.base_name}>{current}>')
    if com == 'shutdown':
        break
    else:
        if root:
            PyXi_do(com, root)
        else:
            PyXi_do(com)

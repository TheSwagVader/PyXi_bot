#this is PyXi bot core

import variables

from interpret import PyXi_do
from logging import record

current = variables.none_root_name
root = False
if variables.default_cls:
    PyXi_do('cls')
if variables.launch_as_root:
    root = True
    current = 'root'
print(f'PyXi bot ver. {variables.version}')
while True:
    com = input(f'{variables.base_name}>{current}>')
    if com == 'shutdown':
        record('shutdown', current)
        break
    else:
        if root:
            PyXi_do(com, root)
            if variables.log_enable:
                record(com, current)
        else:
            PyXi_do(com)
            if variables.log_enable:
                record(com, current)

#this is PyXi bot core

import vars

from interpret import PyXi_do

if vars.default_cls:
    PyXi_do('cls')
print(f'PyXi bot ver. {vars.version}')
while True:
    com = input()
    if com == 'q':
        break
    else:
        PyXi_do(com)
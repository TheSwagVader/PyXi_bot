#this is PyXi bot core

import interpret, vars

print(f'PyXi bot v. {vars.version}')
while True:
    com = input()
    if com == 'test':
        interpret.test()
    if com == 'ver':
        interpret.version()
    elif com == 'q':
        break
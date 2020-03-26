#this is PyXi bot core

import interpret

print('PyXi bot v. 0.0')
while True:
    command = input()
    if command == 'test':
        interpret.test()
    elif command == 'q':
        break
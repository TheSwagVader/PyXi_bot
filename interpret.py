#this file contains defs, needed for PyXi bot

import vars, os

user_db = open(vars.users_file_path, 'r', encoding='utf8')
users = [[],[]] # name, role
#db load
for line in user_db.readlines():
    users[0].append(line[line.find('[')+1:line.find(']')])
    users[1].append(line[line.rfind('[')+1:line.rfind(']')])
user_db.close()
#end db load
def test():
    """
    Test function
    """
    print('Hello, world')

def version():
    """
    Prints current PyXi version
    """
    print(vars.version)

def cls():
    """
    Clears terminal
    """
    os.system('cls' if os.name=='nt' else 'clear')

def status(user):
    """
    Displays user status
    """
    try:
        user_index = users[0].index(user)
        print(f'User: {user}, Role: {users[1][user_index]}')
    except:
        print(f'{user} not registered in database')

def register(username,role):
    """
    Registers new user with role
    """
    addf = open(vars.users_file_path, 'a', encoding='utf8')
    addf.write(f'[{username}][{role}]\n')
    addf.close()
    print(f'Add new user: {username} with role {role}')

def PyXi_do(command):
    """
    PyXi command interpreter
    Do any function or prints error if it not defined
    """
    splt_com = command.split()
    if splt_com[0] == 'test':
        test()
    elif splt_com[0] == 'ver':
        version()
    elif splt_com[0] == 'cls':
        cls()
    elif splt_com[0] == 'status':
        status(splt_com[1])
    elif splt_com[0] == 'register':
        register(splt_com[1], splt_com[2])
    else:
        print(f'{command} not defined')
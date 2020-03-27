#this file contains defs, needed for PyXi bot

import variables, os

user_db = open(variables.users_file_path, 'r', encoding='utf8')
users = [[],[],[]] # name, password, role
#db load
for line in user_db.readlines():
    users[0].append(line[line.find('[')+1:line.find(']')])
    users[1].append(line[line.rfind('[')+1:line.rfind(']')])
    users[2].append(line[line.find('<')+1:line.find('>')])
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
    print(variables.version)

def cls():
    """
    Clears terminal
    """
    os.system('cls' if os.name=='nt' else 'clear')

def status(user, root = False):
    """
    Displays user status
    """
    try:
        user_index = users[0].index(user)
        if root:
            print(f'User: {user}, Password: {users[1][user_index]}, Role: {users[2][user_index]}')
        else:
            if variables.status_block_users.find(user) == -1:
                print(f'User: {user}, Role: {users[2][user_index]}')
            else:
                print('You can see status of this user')
    except:
        print(f'{user} not registered in database')

def register(username, password, role, root = False):
    """
    Registers new user with role
    """
    if root:
        addf = open(variables.users_file_path, 'a', encoding='utf8')
        addf.write(f'[{username}][{password}]<{role}>\n')
        addf.close()
        print(f'Add new user: {username} with password {password} role {role}')
    else:
        print(f'{variables.forrbid_str}')

def help(what = 'none'):
    if what == 'none':
        print(
            'Use help <command> for get info about this command'
        )
    else:
        print(variables.help_dict[what])

#TODO add root enable command
#{def root_enable(who):
#   if who == variables.root_name:
#       print('You are root')
#   else:
#       enter = input('Root password: ')
#       if enter == variables.root_password:
#           print('Root activated')
#           return variables.root_name
#       else:
#           print('Incorrect root password')

def echo(text = ''):
    """
    Just prints text
    """
    print(text)

def PyXi_do(command, root_status = False):
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
        status(splt_com[1], root_status)
    elif splt_com[0] == 'register':
        register(splt_com[1], splt_com[2], splt_com[3])
    elif splt_com[0] == 'help':
        if len(splt_com) == 1:
            help()
        else:
            if variables.command_db.find(splt_com[1]) == -1:
                print(f'{splt_com[1]} not defined')
            else:
                help(splt_com[1])
    elif splt_com[0] == 'echo':
        if len(splt_com) == 1:
            echo()
        else:
            echo(splt_com[1])
    else:
        print(f'{command} not defined')

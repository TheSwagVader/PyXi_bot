#this file contains system vars. Config file?

version = '0.0.6'
default_cls = False
launch_as_root = True
users_file_path = 'users'
base_name = 'PyXi'
root_password = '7c24231a19e369ec8b469d8b809e99fc'
root_name = 'root'
none_root_name = 'none'
status_block_users = 'root.'
log_enable = False
forrbid_str = 'You do not have premission to run this command'
command_db = 'test.cls.version.register.status'
help_dict = {
    'register' : 'register(username, password, role, root = False) : registers new user with role, requires root',
    'status' : 'status(user, root = False) : Displays user status',
    'cls' : 'cls : clears terminal',
    'version' : 'version : prints current PyXi version',
    'test' : 'test : test function',
    'shutdown' : 'shutdown : shutdown PyXi bot'
}

import json

def get_stored_name():
    '''获取已存储用户信息，首次登陆返回None'''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        None
    else:
        return username

def get_new_name():
    '''获取新用户信息'''
    filename = 'username.json'
    username = input('Please Enter your name:')
    with open(filename,'w') as f_obj:
        json.dump(username.title(),f_obj)
    return username # 存储文件中后返回用户名
def greet_user():
    '''模拟游戏启动时，问候用户'''
    username = get_stored_name()
    if username:
        print('welcome back,' + username + '!')
    else:
        username = get_new_name()
        print("I'll remeber you when you come back,"+username.title()+'!')
        
greet_user()

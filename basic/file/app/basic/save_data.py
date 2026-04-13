import json
from pathlib import Path

filename = Path(__file__).with_name('username.json')

# 记住用户名：如果已存储则读取，否则让用户输入并保存
def get_stored_username():
    """获取已存储的用户名"""
    try:
        with open(filename, encoding='utf-8') as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(username, f)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()

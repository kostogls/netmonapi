import os

def credentials():
    username = os.environ["DB_USER"]
    pwd = os.environ["DB_PWD"]
    return username, pwd

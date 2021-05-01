import sys
import cx_Oracle


def connect(username, password):
    if username == '':
        raise ValueError(f'Please fill the username in the credentials file!!')

    if password == '':
        raise ValueError(f'Please fill the password in the credentials file!!')

    login = f'{username}/{password}@artemis.vsnet.gmu.edu:1521/vse18c.vsnet.gmu.edu'

    print('Connecting...')
    conn = cx_Oracle.connect(login)
    print('Connection complete\n')

    return conn

